#!/usr/bin/env python3
"""Build an honest edited walkthrough from two existing browser captures.

No browser automation, recording, cloud service, or fabricated UI is used.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import subprocess, json, textwrap, math

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output'/'demo'
OUT.mkdir(parents=True,exist_ok=True)
ASSETS=OUT/'rendered'; ASSETS.mkdir(exist_ok=True)
W,H=1920,1080
CREAM='#f7f5ed'; GREEN='#254d3b'; INK='#29352e'; MUTED='#7b8271'; SAGE='#e2e8d9'; BLUE='#e6ecec'; RUST='#a36542'; LINE='#d6dbce'
FONT=Path('/System/Library/Fonts/Supplemental')
def font(size,bold=False,serif=False):
    name=('Georgia Bold.ttf' if bold else 'Georgia.ttf') if serif else ('Arial Bold.ttf' if bold else 'Arial.ttf')
    return ImageFont.truetype(str(FONT/name),size)
def txt(d,pos,text,size=36,fill=INK,bold=False,serif=False): d.text(pos,text,font=font(size,bold,serif),fill=fill)
def wrapped(d,pos,text,size,width,fill=INK,bold=False,serif=False,gap=1.25):
    f=font(size,bold,serif); words=text.split(); lines=[]; line=''
    for word in words:
        test=(line+' '+word).strip()
        if d.textbbox((0,0),test,font=f)[2]>width and line: lines.append(line);line=word
        else: line=test
    if line:lines.append(line)
    for i,line in enumerate(lines): d.text((pos[0],pos[1]+int(i*size*gap)),line,font=f,fill=fill)
    return len(lines)*size*gap

def base(label,number):
    im=Image.new('RGB',(W,H),CREAM); d=ImageDraw.Draw(im)
    txt(d,(80,40),'recalllab.',40,bold=True)
    txt(d,(1440,52),label.upper(),18,fill=MUTED,bold=True)
    d.line((80,111,1840,111),fill=LINE,width=2)
    txt(d,(80,895),f'{number:02d} / 08',20,fill=MUTED)
    txt(d,(240,895),'EDITED WALKTHROUGH  ·  REAL CAPTURES + EXPLANATORY CARDS',18,fill=MUTED)
    return im,d

def badge(d,x,y,text,fill=SAGE,color=GREEN):
    f=font(20,True); box=d.textbbox((0,0),text,font=f); tw=box[2]+44
    d.rounded_rectangle((x,y,x+tw,y+42),radius=21,fill=fill)
    d.text((x+22,y+9),text,font=f,fill=color)

def box(d,xy,fill=SAGE):d.rounded_rectangle(xy,radius=24,fill=fill,outline=LINE,width=2)

def arrow(d,start,end,color=MUTED,width=4):
    d.line((*start,*end),fill=color,width=width)
    angle=math.atan2(end[1]-start[1],end[0]-start[0]);l=15
    pts=[end,(end[0]-l*math.cos(angle-.5),end[1]-l*math.sin(angle-.5)),(end[0]-l*math.cos(angle+.5),end[1]-l*math.sin(angle+.5))]
    d.polygon(pts,fill=color)

# 1: Title. Original diagram, not a fabricated product screen.
im,d=base('Product introduction',1)
badge(d,80,170,'MATHEMATICS FOR ECONOMICS')
wrapped(d,(80,255),'Go beyond\nthe answer.'.replace('\n',' '),91,1000,serif=True)
wrapped(d,(84,505),'Explain it. Practise it.\nProve you understand it.'.replace('\n',' '),41,850,fill=MUTED)
for i,label in enumerate(['Attempt','Reviewed hint','Retry','Independent check']):
    x=80+i*435
    box(d,(x,735,x+397,825),SAGE if i!=3 else BLUE)
    txt(d,(x+24,759),label,27,bold=True)
    if i<3:arrow(d,(x+399,780),(x+427,780))
box(d,(1190,175,1835,647),BLUE)
# Plot a cubic with its horizontal tangent at q=2.
d.line((1260,429,1770,429),fill='#b8c7c8',width=2)
d.line((1515,245,1515,565),fill='#c8d3d3',width=2)
pts=[]
for n in range(201):
    q=4*n/200;pts.append((1260+q*127.5,429-(q-2)**3*19.0))
d.line(pts,fill='#607e8e',width=7)
d.ellipse((1505,419,1525,439),fill=RUST,outline='white',width=3)
txt(d,(1550,435),'q = 2',25,fill='#607e8e')
txt(d,(1245,585),'A flat tangent. What can you conclude?',25,fill='#607e8e',serif=True)
im.save(ASSETS/'scene-01.png')

# 2/3: Existing real browser captures, fit to output; original pixels are not edited.
for num,name in [(2,'01-overview.png'),(3,'02-hint.png')]:
    shot=Image.open(OUT/'frames'/name).convert('RGB')
    shot.thumbnail((W,H))
    im=Image.new('RGB',(W,H),CREAM);im.paste(shot,((W-shot.width)//2,0))
    d=ImageDraw.Draw(im)
    d.rounded_rectangle((48,28,760,83),radius=17,fill=GREEN)
    txt(d,(70,44),'ACTUAL BROWSER CAPTURE  ·  LOCAL MODE',22,fill='white',bold=True)
    im.save(ASSETS/f'scene-{num:02}.png')

# 4: Explain the implemented deterministic checker. No fake answer interaction.
im,d=base('Local verification · explained',4)
txt(d,(80,165),'Maths with a checkable result.',67,serif=True)
wrapped(d,(84,270),'Numerical and polynomial answers are checked on the server.',32,1700,fill=MUTED)
box(d,(80,365,910,692),BLUE)
badge(d,115,396,'EXAMPLE FROM THE PRACTICE MODULE',fill='#d4e0e0',color='#536d79')
txt(d,(120,480),'C(q) = 100 + 4q + q²',49,serif=True)
txt(d,(120,565),'C′(3) = 4 + 2(3) = 10',47,serif=True)
box(d,(1000,365,1840,692),SAGE)
for i,label in enumerate(['Restricted mathematical grammar','SymPy equivalence check','Verified or explicitly ungraded result']):
    d.ellipse((1040,412+i*85,1070,442+i*85),fill=GREEN)
    txt(d,(1048,413+i*85),str(i+1),20,fill='white',bold=True)
    txt(d,(1094,410+i*85),label,28,bold=i==0)
txt(d,(84,757),'Learner text is never executed as Python.',33,bold=True)
txt(d,(84,813),'Explanatory card — this is not an additional browser capture.',22,fill=MUTED)
im.save(ASSETS/'scene-04.png')

# 5: Independent-check rules, implemented workflow summary.
im,d=base('Independent check · explained',5)
txt(d,(80,165),'Assisted practice is not the final test.',63,serif=True)
wrapped(d,(84,273),'Five different questions. Feedback held until the check is complete.',33,1700,fill=MUTED)
for i in range(5):
    x=80+i*355
    box(d,(x,390,x+326,570),SAGE)
    txt(d,(x+28,421),f'0{i+1}',59,fill=GREEN,serif=True)
    txt(d,(x+28,512),'Answer recorded',24,fill=MUTED)
    if i<4:arrow(d,(x+331,480),(x+347,480))
for x,t,sub in [(80,'No hints during check','Assistance stays in practice.'),(680,'Marks withheld','Results open after completion.'),(1280,'Progress kept separate','Saved work and review dates.')]:
    txt(d,(x,660),t,30,bold=True)
    wrapped(d,(x,718),sub,28,530,fill=MUTED)
txt(d,(84,815),'Implemented workflow summary — scores and learner outcomes are not fabricated.',23,fill=MUTED)
im.save(ASSETS/'scene-05.png')

# 6: Actual architecture, drawn as an explanatory diagram.
im,d=base('MCP architecture · explained',6)
txt(d,(80,165),'Four real tools. One durable learning loop.',62,serif=True)
items=[(80,325,560,510,'React + TypeScript','Official MCP browser client',SAGE),(720,325,1220,510,'FastAPI + FastMCP','Streamable HTTP · /mcp/',BLUE),(1380,325,1840,510,'StudyService','Server-enforced workflow',SAGE)]
for x1,y1,x2,y2,t,s,c in items:
    box(d,(x1,y1,x2,y2),c);txt(d,(x1+30,y1+40),t,32,bold=True);wrapped(d,(x1+30,y1+103),s,25,x2-x1-60,fill=MUTED)
arrow(d,(567,417),(707,417));arrow(d,(1227,417),(1367,417))
box(d,(80,615,1175,790),'#efede2')
txt(d,(115,645),'start_session   ·   submit_attempt',30,bold=True)
txt(d,(115,710),'review_question   ·   get_progress',30,bold=True)
arrow(d,(1600,520),(1600,605))
box(d,(1310,615,1840,790),BLUE)
txt(d,(1342,650),'SQLite + local maths',33,bold=True)
txt(d,(1342,712),'Persisted attempts · request IDs',24,fill=MUTED)
im.save(ASSETS/'scene-06.png')

# 7: Honest current boundaries.
im,d=base('Current status · transparent',7)
txt(d,(80,165),'Working locally. Clear about the boundary.',60,serif=True)
box(d,(80,300,915,787),SAGE);box(d,(1000,300,1840,787),'#efe6d9')
badge(d,120,340,'WORKS TODAY')
for i,t in enumerate(['Attempt-first learning loop','Local symbolic maths checks','Reviewed hints and source notes','Saved sessions and independent checks']):
    txt(d,(120,430+i*72),'•  '+t,29,bold=i==0)
badge(d,1040,340,'CLOUD ASSESSMENT OFF',fill='#e2cdb8',color='#765137')
wrapped(d,(1040,430),'Bedrock Nova Lite adapter implemented. AWS account restriction prevents invocation.',31,730)
wrapped(d,(1040,590),'Conceptual explanations are saved for self-review, with no automatic grade.',29,730,fill=MUTED)
wrapped(d,(1040,715),'No live inference or model accuracy claim.',26,730,fill=RUST,bold=True)
im.save(ASSETS/'scene-07.png')

# 8: Evidence and learning agenda.
im,d=base('Evidence + next steps',8)
txt(d,(80,165),'Make understanding visible.',76,serif=True)
box(d,(80,330,900,700),SAGE)
txt(d,(125,380),'Verified implementation',39,bold=True)
for i,t in enumerate(['Automated release checks','Real MCP browser workflows','Distinct independent-check questions']):txt(d,(125,465+i*65),'•  '+t,28)
box(d,(995,330,1840,700),BLUE)
txt(d,(1040,380),'Next evidence to collect',39,bold=True)
for i,t in enumerate(['Independent rubric-label review','Live conceptual benchmark','Five-student pilot + next-day check']):txt(d,(1040,465+i*65),'•  '+t,28)
txt(d,(84,755),'Browser simulation of an Alexa+ use case · Real MCP integration',30,bold=True)
txt(d,(84,819),'No native Alexa+ integration or measured learning-gain claim.',23,fill=MUTED)
im.save(ASSETS/'scene-08.png')

scenes=[
(1,[
'Recognising a worked answer is different from producing one yourself.',
'RecallLab is a study companion for mathematics for economics, designed around an attempt, a reviewed hint, a retry, and a separate independent check.',
'This edited walkthrough uses two real browser captures and explanatory cards.']),
(2,[
'The dashboard introduces a useful misconception: does a zero derivative always mean a maximum?',
'The first module has twelve concepts, twenty-five practice questions, and five separate check questions.',
'Optional speech input leaves an editable answer; typing remains available.']),
(3,[
'Here is an actual saved attempt, followed by the first reviewed hint.',
'The cubic graph is flat at two, but continues to rise. A stationary point alone does not establish a maximum.',
'The interface says this explanation is not automatically graded, because cloud assessment is off.']),
(4,[
'Mathematical answers follow a different path: numerical and polynomial responses are checked locally using a restricted grammar and SymPy.',
'Learner text is never executed as Python.',
'Hints, original source notes, and solution reveals become available after an attempt, and assistance is recorded.']),
(5,[
'An independent check uses five distinct questions. Hints and marks stay hidden until every answer is recorded.',
'Practice, assistance, and independent results are tracked separately, with saved sessions and a suggested review queue.']),
(6,[
'Under the interface, the official MCP client calls four real tools over Streamable HTTP.',
'FastAPI and FastMCP connect the learning workflow to SQLite and deterministic maths checking.',
'Idempotent request IDs prevent duplicate submissions from creating duplicate assessments.']),
(7,[
'A Bedrock Nova Lite adapter is implemented, but AWS currently restricts model invocation for this account.',
'The demo therefore runs in honest local mode, with conceptual explanations saved for self review.',
'There is no claim of successful cloud inference, model accuracy, or measured learning gains.']),
(8,[
'The application passes automated release checks and verified browser workflows.',
'Next come independent label review, the live conceptual benchmark, and a five student pilot with a next day check.',
'RecallLab is a browser simulation of a possible Alexa Plus experience, with real MCP integration.',
'Explain it. Practise it. Prove you understand it.'])]

segments=[];time=0;captions=[];script=['# RecallLab demo narration','', 'Edited walkthrough: two real browser captures plus original explanatory cards.', 'English synthetic narration. No successful cloud response or live interaction is simulated.', '']
for scene, sentences in scenes:
    for sentence in sentences:
        idx=len(segments)+1;stem=f'part-{idx:02}'
        textfile=ASSETS/(stem+'.txt'); textfile.write_text(sentence)
        audio=ASSETS/(stem+'.aiff')
        if not audio.exists():subprocess.run(['/usr/bin/say','-v','Samantha','-r','177','-f',str(textfile),'-o',str(audio)],check=True)
        info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','json',str(audio)]))
        adur=float(info['format']['duration']);duration=math.ceil((adur+.50)*30)/30
        # Original slide plus clearly separate English captions.
        frame=Image.open(ASSETS/f'scene-{scene:02}.png').convert('RGB');d=ImageDraw.Draw(frame)
        d.rectangle((0,941,W,H),fill=GREEN)
        # Exactly the spoken sentence. Limit line length visually to ~100 characters.
        lines=textwrap.wrap(sentence,108)
        start=962 if len(lines)<=2 else 950
        fs=31 if len(lines)<=2 else 27
        for j,line in enumerate(lines):
            f=font(fs);bb=d.textbbox((0,0),line,font=f);d.text(((W-bb[2])/2,start+j*(fs+8)),line,font=f,fill='#fffdf5')
        d.rectangle((0,H-7,int(W*(time/(150))),H),fill='#8fa77b')
        png=ASSETS/(stem+'.png');frame.save(png)
        clip=ASSETS/(stem+'.mp4')
        subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-loop','1','-framerate','30','-i',str(png),'-i',str(audio),'-t',str(duration),'-vf','fade=t=in:st=0:d=0.16','-af','apad=pad_dur=1','-c:v','libx264','-preset','veryfast','-tune','stillimage','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-ar','48000','-ac','2','-movflags','+faststart',str(clip)],check=True)
        segments.append(clip);captions.append((time+.04,time+adur+.2,sentence));script.extend([f'{time:06.2f}s · Scene {scene}',sentence,'']);time+=duration
        print(f'{stem}: scene {scene}, {duration:.2f}s, total {time:.2f}s',flush=True)

concat=ASSETS/'concat.txt';concat.write_text('\n'.join("file '"+str(p).replace("'","'\\''")+"'" for p in segments)+'\n')
video=OUT/'recalllab-demo.mp4'
subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-f','concat','-safe','0','-i',str(concat),'-c','copy','-movflags','+faststart',str(video)],check=True)
def tc(s):
    ms=round(s*1000);h,ms=divmod(ms,3600000);m,ms=divmod(ms,60000);sec,ms=divmod(ms,1000);return f'{h:02}:{m:02}:{sec:02},{ms:03}'
(OUT/'recalllab-demo.srt').write_text('\n\n'.join(f'{i}\n{tc(start)} --> {tc(end)}\n{text}' for i,(start,end,text) in enumerate(captions,1))+'\n')
(OUT/'narration.md').write_text('\n'.join(script)+'\n')
(OUT/'provenance.md').write_text('''# Demo provenance\n\nThis is an edited walkthrough, not a continuous screen recording. It uses two actual RecallLab browser captures (`frames/01-overview.png`, `frames/02-hint.png`) and original explanatory title, workflow and architecture cards drawn with Pillow. Captures are resized to fit; no product states are fabricated. English narration is synthesised locally using macOS Samantha. Captions are burned in, with a matching SRT sidecar. No music, third-party footage, inbox, AWS account data or credentials appear.\n\nThe video states that cloud assessment is disabled and AWS currently prevents model invocation. It claims no live inference, conceptual-model accuracy, student pilot, learning gain or native Alexa+ integration. Explanatory cards describe implemented workflows; they do not pretend to be additional captured UI.\n''')
# Contact sheet of authored scenes, with caption-safe layouts.
thumbs=[]
for i in range(1,9):
    im=Image.open(ASSETS/f'scene-{i:02}.png');im.thumbnail((640,360));thumbs.append(im)
contact=Image.new('RGB',(1280,1440),CREAM)
for n,im in enumerate(thumbs):contact.paste(im,((n%2)*640,(n//2)*360))
contact.save(OUT/'contact-sheet.jpg',quality=92)
meta=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration,size:stream=codec_name,width,height,sample_rate,channels','-of','json',str(video)]))
(OUT/'verification.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2),flush=True)
if float(meta['format']['duration'])>=180:raise SystemExit('Video exceeds three minutes')
print(video,flush=True)
