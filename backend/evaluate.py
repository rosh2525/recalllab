"""Run candidate conceptual evaluations only on explicit opt-in to actual model calls."""
import argparse
import json
import time
from pathlib import Path
from recalllab.content import BY_ID
from recalllab.grading import Assessor
parser=argparse.ArgumentParser()
parser.add_argument('--live',action='store_true',help='Use the configured Bedrock account; requires explicit cloud enablement.')
parser.add_argument('--limit',type=int,default=60)
parser.add_argument('--output',type=Path,default=Path('evaluation/latest-report.json'))
args=parser.parse_args()
cases=json.loads((Path(__file__).resolve().parents[1]/'evaluation'/'conceptual.json').read_text())
if not args.live:
    print(json.dumps({'case_count':len(cases),'live_evaluation':'not run','reason':'No cloud calls without --live and RECALLLAB_ENABLE_BEDROCK=1. Labels require independent educator review.'},indent=2));raise SystemExit(0)
a=Assessor()
if not a.live:parser.error('Set RECALLLAB_ENABLE_BEDROCK=1 only after verifying access and credit/budget coverage.')
if not 1<=args.limit<=60:parser.error('--limit must be between 1 and 60')
results=[]
for case in cases[:args.limit]:
    started=time.perf_counter()
    result=a.assess(BY_ID[case['question_id']],case['answer'])
    results.append({'id':case['id'],'expected':case['expected_status'],'actual':result['status'],'method':result['method'],'latency_ms':round((time.perf_counter()-started)*1000),'usage':result.get('usage',{})})
    if result['method']=='bedrock_unavailable':break
completed=[r for r in results if r['method']=='bedrock']
report={'model':a.model,'region':a.region,'labels':'developer-authored; independent review pending','attempted':len(results),'completed':len(completed),'completion_rate':len(completed)/len(results),'total_usage':{key:sum(r['usage'].get(key,0) for r in results) for key in ('input_tokens','output_tokens')},'agreement':sum(r['expected']==r['actual'] for r in completed)/len(completed) if completed else None,'results':results}
args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='results'},indent=2))
