from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from tortoise.contrib.fastapi import register_tortoise

from .exceptions import BaseLeakyException, UserExistsError
from .oauth.exceptions import AuthError, ProtoException
from .oauth.routes import router as auth_router
from .utils.settings import TORTOISE_ORM
from .users_management.routes import router as users_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(users_router)
app.mount('/static', StaticFiles(directory=Path(__file__).parent / 'static'), name='static')

app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost/"
            "http://localhost:80/",
            "http://localhost:8000/"
        ],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
)


@app.exception_handler(UserExistsError)
async def process_user_exist_error(request: Request, exc: UserExistsError):
    return ORJSONResponse(
            status_code=exc.status_code,
            content={"error": exc.error, "description": exc.description},
            headers={"Location": f"/users/{exc.user_id}"}
    )


@app.exception_handler(BaseLeakyException)
async def process_exception(request: Request, exc: BaseLeakyException):
    return ORJSONResponse(
            status_code=exc.status_code,
            content={"error": exc.error, "description": exc.description}
    )


@app.exception_handler(AuthError)
async def process_auth_exception(request: Request, exc: AuthError):
    return RedirectResponse(await exc.get_redirect_uri(), status_code=exc.status_code)


@app.exception_handler(ProtoException)
async def process_exception(request: Request, exc: ProtoException):
    return ORJSONResponse(status_code=400, content=exc.to_dict(),
                          headers={'Cache-Control': 'no-store', 'Pragma': 'no-cache'})


register_tortoise(app, config=TORTOISE_ORM, generate_schemas=True)
