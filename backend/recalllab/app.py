from contextlib import asynccontextmanager
from pathlib import Path
from typing import Literal
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.trustedhost import TrustedHostMiddleware
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings
from .content import MODULE_ID, module_info
from .service import StudyService, StudyError

service=StudyService()
mcp=FastMCP('RecallLab',stateless_http=True,json_response=True,streamable_http_path='/',transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=True,allowed_hosts=['127.0.0.1:*','localhost:*','testserver'],allowed_origins=['http://127.0.0.1:8000','http://localhost:8000','http://127.0.0.1:5173','http://localhost:5173']))

@mcp.tool()
def start_session(module_id:str=MODULE_ID,mode:Literal['practice','check']='practice',resume_id:str|None=None,track:str='all')->dict:
    """Start or resume the local learner's course. Check mode withholds feedback until completion."""
    return service.start_session(module_id,mode,resume_id,track)

@mcp.tool()
def submit_attempt(study_session_id:str,question_id:str,request_id:str,answer:str)->dict:
    """Save and assess an answer once. Reuse request_id for an identical retry."""
    return service.submit_attempt(study_session_id,question_id,request_id,answer)

@mcp.tool()
def review_question(study_session_id:str,question_id:str,action:Literal['hint','solution','next'])->dict:
    """Request the next reviewed hint, reveal an assisted solution, or advance after an attempt."""
    return service.review_question(study_session_id,question_id,action)

@mcp.tool()
def get_progress(module_id:str=MODULE_ID)->dict:
    """Read practice history, independent results, and tomorrow's review queue. Never exposes unfinished check marks."""
    return service.get_progress(module_id)

@asynccontextmanager
async def lifespan(app):
    async with mcp.session_manager.run(): yield

app=FastAPI(title='RecallLab',version='0.1.0',lifespan=lifespan)
app.add_middleware(TrustedHostMiddleware,allowed_hosts=['127.0.0.1','localhost','testserver'])

@app.middleware('http')
async def local_origin(request:Request,call_next):
    origin=request.headers.get('origin')
    if origin and origin not in ('http://127.0.0.1:8000','http://localhost:8000','http://127.0.0.1:5173','http://localhost:5173'):
        return JSONResponse({'error':'This local application does not accept that origin.'},status_code=403)
    if request.headers.get('content-length','').isdigit() and int(request.headers['content-length'])>32768:
        return JSONResponse({'error':'Request too large.'},status_code=413)
    response=await call_next(request)
    response.headers['X-Content-Type-Options']='nosniff'
    response.headers['Referrer-Policy']='no-referrer'
    response.headers['Permissions-Policy']='microphone=(self)'
    response.headers['Content-Security-Policy']="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'"
    return response

@app.get('/api/module')
def module(): return module_info()

@app.get('/api/health')
def health(): return {'ok':True,'version':'0.1.0','model_status':service.assessor.status(),'storage':'local SQLite','mcp_endpoint':'/mcp/'}

app.mount('/mcp',mcp.streamable_http_app())
frontend=Path(__file__).resolve().parents[2]/'frontend'/'dist'
if frontend.is_dir(): app.mount('/',StaticFiles(directory=str(frontend),html=True),name='frontend')
