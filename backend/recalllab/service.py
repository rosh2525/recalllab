"""Transactional, local single-learner study state. Protocol sessions are unrelated."""
import json
import os
import sqlite3
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from contextlib import contextmanager
from .content import BY_ID, CONCEPTS, MODULE_ID, PRACTICE_QUESTIONS as QUESTIONS, CHECK_QUESTIONS, SOURCES, TRACKS, VERSION, public_question
from .grading import Assessor

class StudyError(ValueError): pass

def now(): return datetime.now(timezone.utc).isoformat()
class StudyService:
    def __init__(self,path=None,assessor=None):
        self.path=str(path or os.getenv('RECALLLAB_DB',str(Path(__file__).resolve().parents[2]/'data'/'recalllab.sqlite3')))
        Path(self.path).parent.mkdir(parents=True,exist_ok=True)
        self.assessor=assessor or Assessor()
        with self.connect() as db:
            db.executescript('''PRAGMA journal_mode=WAL;
            CREATE TABLE IF NOT EXISTS sessions(id TEXT PRIMARY KEY,mode TEXT NOT NULL,track TEXT NOT NULL,question_ids TEXT NOT NULL,position INTEGER NOT NULL DEFAULT 0,hints TEXT NOT NULL DEFAULT '{}',assisted TEXT NOT NULL DEFAULT '[]',complete INTEGER NOT NULL DEFAULT 0,created_at TEXT NOT NULL,version TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS attempts(id TEXT PRIMARY KEY,session_id TEXT NOT NULL,question_id TEXT NOT NULL,request_id TEXT NOT NULL,answer TEXT NOT NULL,assessment TEXT NOT NULL,assisted INTEGER NOT NULL,created_at TEXT NOT NULL,UNIQUE(session_id,request_id));
            CREATE INDEX IF NOT EXISTS attempt_session ON attempts(session_id,question_id);
            ''')
    @contextmanager
    def connect(self):
        db=sqlite3.connect(self.path,timeout=30); db.row_factory=sqlite3.Row
        try:
            with db: yield db
        finally: db.close()
    def _session(self,db,id):
        s=db.execute('SELECT * FROM sessions WHERE id=?',(id,)).fetchone()
        if not s: raise StudyError('Session not found.')
        return dict(s)
    def _attempts(self,db,s):
        rows=db.execute('SELECT * FROM attempts WHERE session_id=? ORDER BY rowid',(s['id'],)).fetchall()
        return [{'id':r['id'],'question_id':r['question_id'],'answer':r['answer'],'assisted':bool(r['assisted']),'created_at':r['created_at'],**({'assessment':json.loads(r['assessment'])} if s['mode']=='practice' or s['complete'] else {})} for r in rows]
    def _view(self,db,s):
        ids=json.loads(s['question_ids']); q=BY_ID[ids[min(s['position'],len(ids)-1)]]
        attempts=self._attempts(db,s); answered=[a for a in attempts if a['question_id']==q['id']]
        payload={'study_session_id':s['id'],'mode':s['mode'],'track':s['track'],'position':s['position'],'total':len(ids),'complete':bool(s['complete']),'current_question':None if s['complete'] else public_question(q),'attempts':attempts,'assisted_question_ids':json.loads(s['assisted']),'hint_count':json.loads(s['hints']).get(q['id'],0),'content_version':s['version'],'created_at':s['created_at']}
        if s['mode']=='practice' and answered:
            payload['sources']=[SOURCES[k] for k in q['source_ids']]
            payload['visible_hints']=q['hints'][:payload['hint_count']]
        if s['complete']:
            payload['review']=[{'question':public_question(BY_ID[k]),'solution':BY_ID[k]['solution'],'sources':[SOURCES[x] for x in BY_ID[k]['source_ids']]} for k in ids]
        return payload
    def start_session(self,module_id=MODULE_ID,mode='practice',resume_id=None,track='all'):
        if module_id!=MODULE_ID or mode not in ('practice','check'): raise StudyError('Choose the available module and a valid study mode.')
        with self.connect() as db:
            if resume_id: return self._view(db,self._session(db,resume_id))
            selected=next((t for t in TRACKS if t['id']==track),None)
            if not selected: raise StudyError('Unknown learning path.')
            ids=[q['id'] for q in QUESTIONS if q['concept_id'] in selected['concepts']]
            if mode=='check':
                # Fixed reviewed parallel questions, not generated answers or a reused practice sequence.
                check_ids=[q['id'] for q in CHECK_QUESTIONS]
                ids=[k for k in check_ids if BY_ID[k]['concept_id'] in selected['concepts']] or [q['id'] for q in CHECK_QUESTIONS[:3]]
            id=uuid.uuid4().hex
            db.execute('INSERT INTO sessions(id,mode,track,question_ids,created_at,version) VALUES(?,?,?,?,?,?)',(id,mode,track,json.dumps(ids),now(),VERSION))
            return self._view(db,self._session(db,id))
    def submit_attempt(self,study_session_id,question_id,request_id,answer):
        if not isinstance(answer,str) or not 1<=len(answer.strip())<=3000: raise StudyError('Enter an answer of 1–3000 characters.')
        if not isinstance(request_id,str) or not 1<=len(request_id)<=100: raise StudyError('A request ID is required.')
        answer=answer.strip()
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            s=self._session(db,study_session_id)
            prev=db.execute('SELECT * FROM attempts WHERE session_id=? AND request_id=?',(s['id'],request_id)).fetchone()
            if prev:
                if prev['question_id']!=question_id or prev['answer']!=answer: raise StudyError('This request ID was already used for another answer.')
                return self._view(db,s)
            ids=json.loads(s['question_ids'])
            if s['complete'] or ids[s['position']]!=question_id: raise StudyError('That question is not the current question.')
            if s['mode']=='check' and db.execute('SELECT 1 FROM attempts WHERE session_id=? AND question_id=?',(s['id'],question_id)).fetchone(): raise StudyError('This check answer has already been recorded.')
            q=BY_ID[question_id]
            # Global daily model-call allowance; all attempts count so failures cannot bypass the cap.
            daily=db.execute("SELECT COUNT(*) FROM attempts WHERE created_at>=?",(datetime.now(timezone.utc).date().isoformat(),)).fetchone()[0]
            if q['kind']=='concept' and daily>=int(os.getenv('RECALLLAB_DAILY_ATTEMPT_LIMIT','100')):
                assessment={'status':'unable_to_assess','feedback':'The daily assessment limit has been reached. Your answer is saved for self-review.','method':'limit','usage':{}}
            else: assessment=self.assessor.assess(q,answer)
            assisted=question_id in json.loads(s['assisted'])
            db.execute('INSERT INTO attempts VALUES(?,?,?,?,?,?,?,?)',(uuid.uuid4().hex,s['id'],question_id,request_id,answer,json.dumps(assessment),int(assisted),now()))
            return self._view(db,self._session(db,s['id']))
    def review_question(self,study_session_id,question_id,action):
        if action not in ('hint','solution','next'): raise StudyError('Unknown review action.')
        with self.connect() as db:
            db.execute('BEGIN IMMEDIATE'); s=self._session(db,study_session_id); ids=json.loads(s['question_ids'])
            if s['complete'] or ids[s['position']]!=question_id: raise StudyError('That question is not the current question.')
            attempted=db.execute('SELECT 1 FROM attempts WHERE session_id=? AND question_id=?',(s['id'],question_id)).fetchone()
            if not attempted: raise StudyError('Make an attempt before opening feedback or moving on.')
            if s['mode']=='check' and action!='next': raise StudyError('Hints and solutions are available after the independent check finishes.')
            if action=='next':
                pos=s['position']+1; db.execute('UPDATE sessions SET position=?,complete=? WHERE id=?',(pos,int(pos>=len(ids)),s['id']))
            else:
                assisted=set(json.loads(s['assisted'])); assisted.add(question_id)
                hints=json.loads(s['hints'])
                if action=='hint': hints[question_id]=min(3,hints.get(question_id,0)+1)
                db.execute('UPDATE sessions SET hints=?,assisted=? WHERE id=?',(json.dumps(hints),json.dumps(sorted(assisted)),s['id']))
                db.execute('UPDATE attempts SET assisted=1 WHERE session_id=? AND question_id=?',(s['id'],question_id))
            result=self._view(db,self._session(db,s['id']))
            if action=='solution': result['solution']=BY_ID[question_id]['solution']
            return result
    def get_progress(self,module_id=MODULE_ID):
        if module_id!=MODULE_ID: raise StudyError('Unknown module.')
        with self.connect() as db:
            sessions=[dict(s) for s in db.execute('SELECT * FROM sessions ORDER BY created_at DESC')]
            history=[]; latest={}; review_latest={}; checks=[]
            for s in sessions:
                attempts=self._attempts(db,s)
                history.append({'study_session_id':s['id'],'mode':s['mode'],'track':s['track'],'complete':bool(s['complete']),'position':s['position'],'total':len(json.loads(s['question_ids'])),'created_at':s['created_at']})
                # Never reveal a pending check's marks through the progress tool.
                if s['mode']=='check' and not s['complete']: continue
                for a in attempts:
                    old=review_latest.get(a['question_id'])
                    if old is None or a['created_at']>old['created_at']: review_latest[a['question_id']]=a
                    if s['mode']=='practice':
                        old=latest.get(a['question_id'])
                        if old is None or a['created_at']>old['created_at']: latest[a['question_id']]=a
                if s['mode']=='check' and s['complete']: checks.extend(attempts)
            results=list(latest.values()); correct=sum(a['assessment']['status']=='correct' for a in results)
            review=[{'question_id':k,'concept_id':BY_ID[k]['concept_id'],'title':SOURCES[BY_ID[k]['concept_id']]['title'],'status':a['assessment']['status'],'assisted':a['assisted'],'due_at':(datetime.fromisoformat(a['created_at'])+timedelta(days=1)).isoformat()} for k,a in review_latest.items() if a['assessment']['status']!='correct' or a['assisted']]
            return {'sessions':history,'attempted_questions':len(results),'correct_questions':correct,'assisted_questions':sum(a['assisted'] for a in results),'independent_checks':len([s for s in sessions if s['mode']=='check' and s['complete']]),'independent_correct':sum(a['assessment']['status']=='correct' for a in checks),'independent_total':len(checks),'review_queue':review,'model_status':self.assessor.status()}
