import base64
from pathlib import Path
from random import getrandbits
from urllib import parse

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse, ORJSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .settings import __settings
from .utils import http_client, menu

app = FastAPI()
app.mount('/static', StaticFiles(directory=Path(__file__).parent / 'static'), name='static')

templates = Jinja2Templates(directory=(Path(__file__).parent / 'templates').as_posix())

origins = [
    "http://localhost"
    "http://localhost:80",
    "http://localhost:8000"
]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

localhost = "http://localhost:8000"


@app.get('/dashboard', response_class=HTMLResponse)
async def dashboard_page(request: Request):
    return templates.TemplateResponse(request=request, name="dashboard.html", context={'menu_categories': menu})


auth_state = ''


@app.get('/auth/callback')
async def auth_callback(code: str = None,
                        state: str = None,
                        error: str = None,
                        description: str = None):
    print(code, state, error, description)
    if error:
        raise HTTPException(status_code=400, detail={'error': error, 'description': description})
    query = {'grant_type': 'authorization_code',
             'code': code,
             'redirect_uri': f'{localhost}/auth/callback',
             'client_id': __settings.client_id}
    resp = (await http_client.post(f'{__settings.auth_server_address}/oauth/token', data=query,
                                   headers={'Authorization': f'Bearer {__settings.client_secret}'})).json()
    global auth_state
    if resp['state'] == auth_state:
        return RedirectResponse('/dashboard')
    raise HTTPException(status_code=400, detail={'error': 'invalid_state',
                                                 'description': 'State in response does not match state of the client'})


@app.get('/auth')
async def login_to_dashboard():
    global auth_state
    auth_state = base64.b64encode(f'{getrandbits(32)}'.encode()).decode('ascii')
    query = parse.urlencode({'response_type': 'code',
                             'client_id': __settings.client_id,
                             'redirect_uri': f'{localhost}/auth/callback',
                             'state': auth_state,
                             'scope': __settings.required_scopes})
    return RedirectResponse(f'{__settings.auth_server_address}/oauth/authorize?{query}')


@app.get('/')
async def redirect_to_login():
    return RedirectResponse('/auth')


@app.exception_handler(HTTPException)
async def process_exeption(request: Request, exp: HTTPException):
    return ORJSONResponse(status_code=exp.status_code, content=exp.detail)
