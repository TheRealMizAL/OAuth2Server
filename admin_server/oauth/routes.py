import base64
import datetime
import random
from typing import Annotated
from urllib import parse
from uuid import uuid4

from fastapi import APIRouter, Request, Header, Form, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import UUID4, EmailStr
from tortoise.transactions import in_transaction

from .exceptions import AccessDeniedError, InvalidScopeError, UnsupportedResponseTypeError, UnauthorizedClientError
from .exceptions import (InvalidResponseTypesException, NoRedirectURIsException, SussySoftwareException,
                         NoInitialTokenException, PublicClientNotAllowedException, InvalidSoftwareStatement,
                         MultipleGrantTypesNotAllowedException, InvalidMetadataURI, TokenInvalidRequest,
                         TokenAccessDenied)
from .schemas import types_mapping
from ..models import Creds, Clients
from ..schemas import ClientRegistrationRequest, ClientInformationResponse, HttpsUrl, GrantTypes
from ..utils.security import verify_password, oauth_scopes, Policies, get_password_hash, create_jwt
from ..utils.templating import templates

router = APIRouter(prefix='/oauth')


@router.get('/authorize')
async def login_page(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")


async def try_to_auth():
    pass


async def validate_client(client: Clients,
                          scope: str,
                          response_type: str,
                          redirect_uri: HttpsUrl):
    pass


@router.post('/authorize')
async def try_to_auth_router(login: Annotated[EmailStr, Form()],
                             passwd: Annotated[str, Form()],
                             scope: str,
                             response_type: str,
                             client_id: UUID4,
                             redirect_uri: HttpsUrl,
                             state: str | None = None,
                             nonce: str | None = None):
    if response_type != "code":
        raise UnsupportedResponseTypeError(redirect_uri, state)

    async with in_transaction() as conn:
        if not (client := await Clients.get_or_none(id=client_id)):
            raise UnauthorizedClientError(redirect_uri, state)
        await validate_client(client, scope, response_type, redirect_uri)

        scopes = set(scope.split(sep=' '))
        if len(scopes) != len(scopes & set(oauth_scopes)):
            raise InvalidScopeError(redirect_uri, state)

        if not (creds_in_db := await Creds.get_or_none(login=login, using_db=conn)):
            raise AccessDeniedError(redirect_uri=redirect_uri, state=state)
        if not verify_password(passwd, creds_in_db.passwd):
            raise AccessDeniedError(redirect_uri=redirect_uri, state=state)

        query = {'code': base64.b64encode(f'{random.getrandbits(32)}'.encode()).decode('ascii')}
        if state:
            query['state'] = state
        return RedirectResponse(f"{redirect_uri}?{parse.urlencode(query)}",
                                status_code=302)


async def exchange_client_creds_on_token(client_id: str, secret: str, scope: str):
    async with in_transaction() as conn:
        if client := await Clients.get_or_none(client_id=client_id, client_secret=get_password_hash(secret),
                                               using_db=conn):
            await create_jwt(
                    {'client_id': client_id,
                     'scope': scope
                     }
            )
        raise TokenAccessDenied()


async def exchange_code_for_token(code, redirect_uri, client_id):
    pass


@router.post('/token')
async def get_token(response: Response, request: Request,
                    grant_type: Annotated[GrantTypes, Form()],
                    code: Annotated[str, Form()] = None,
                    scope: Annotated[str, Form()] = None,
                    redirect_uri: Annotated[HttpsUrl, Form()] = None,
                    client_id: Annotated[UUID4, Form()] = None,
                    authorization: Annotated[str, Header()] = None):
    response.headers.append('Cache-Control', 'no-store')
    response.headers.append('Pragma', 'no-cache')

    if not authorization:
        raise TokenAccessDenied()

    match grant_type:
        case "client_credentials":
            base64string = authorization.split()[1]
            try:
                client_id, client_secret = base64.b64decode(base64string).decode('utf-8').split(':')[:2]
                return await exchange_client_creds_on_token(client_id, client_secret, scope)
            except ValueError:
                raise TokenAccessDenied()

        case "authorization_code":
            if not code or scope:
                raise TokenInvalidRequest()
            return exchange_code_for_token(client_id, code, redirect_uri)


@router.post('/refresh_token')
async def get_refresh_token():
    pass


async def process_registration(registration_request: ClientRegistrationRequest,
                               allow_public_clients_policy: bool = True,
                               allow_multiple_grant_types_policy: bool = True,
                               require_software_statement: bool = True,
                               strict_uris: bool = True,
                               trust_content: bool = True,
                               override_on_diff: bool = True,
                               allow_multi_instance_clients: bool = True,
                               client_secret_len: int = 128,
                               client_secret_exp_days: int = 30):
    if not allow_public_clients_policy and registration_request.token_endpoint_auth_method == "none":
        raise PublicClientNotAllowedException
    if not allow_multiple_grant_types_policy and len(registration_request.grant_types) > 1:
        raise MultipleGrantTypesNotAllowedException

    if require_software_statement and not registration_request.software_statement:
        raise InvalidSoftwareStatement

    for grant_type, resp_type in types_mapping.items():
        if resp_type in registration_request.response_types and grant_type not in registration_request.grant_types:
            raise InvalidResponseTypesException

    if set(registration_request.grant_types) & {"authorization_code",
                                                "implicit"} and not registration_request.redirect_uris:
        raise NoRedirectURIsException

    sites = {f'{uri.scheme}://{uri.host}' for uri in registration_request.redirect_uris}
    if strict_uris:
        properties = {f'{v.scheme}://{v.host}' for k, v in registration_request.model_dump().items() if
                      'uri' in k and v and k != 'redirect_uris'}
        if len(properties | sites) != len(sites):
            raise InvalidMetadataURI


    if not allow_multi_instance_clients:
        if not registration_request.software_id and not registration_request.software_version:
            raise SussySoftwareException

    response_model = ClientInformationResponse(client_id=uuid4(),
                                               client_id_issued_at=datetime.datetime.now(),
                                               **registration_request.model_dump(exclude_unset=True))
    if registration_request.token_endpoint_auth_method != "none":
        response_model.client_secret = get_password_hash(
                base64.b64encode(f'{random.getrandbits(client_secret_len)}'.encode()).decode(
                        'ascii'))
        response_model.client_secret_expires_at = datetime.datetime.now() + datetime.timedelta(
                days=client_secret_exp_days)

    async with in_transaction() as conn:
        if not allow_multi_instance_clients and await Clients.exists(software_id=registration_request.software_id,
                                                                     software_version=registration_request.software_version,
                                                                     using_db=conn):
            raise SussySoftwareException
        model_json = response_model.model_dump(by_alias=True, exclude_unset=True)

        client_main = {k: v for k, v in model_json.items() if '#' not in k}
        for k in ['client_name', 'tos_uri', 'policy_uri', 'logo_uri', 'client_uri', 'redirect_uris', 'grant_types',
                  'response_types', 'contacts', 'jwks']:
            client_main.pop(k, None)

        new_client = await Clients.create(**client_main, using_db=conn)
        for key in ['redirect_uris', 'grant_types', 'response_types', 'contacts', 'jwks']:
            if key in model_json:
                model_cls = getattr(new_client, key).remote_model
                models = [model_cls(client_id=new_client.client_id, **{key[:-1]: i})
                          for i in model_json[key]]
                await model_cls.bulk_create(models, using_db=conn)

        for key in ['client_name', 'tos_uri', 'policy_uri', 'logo_uri', 'client_uri']:
            model_dict = {k: v for k, v in model_json.items() if key in k}
            await getattr(new_client, key + 's').remote_model.create(**model_dict, client_id=new_client.client_id,
                                                                     using_db=conn)

    return response_model.model_dump(by_alias=True, exclude_unset=True)


@router.post('/register',
             response_model=ClientInformationResponse,
             response_model_exclude_unset=True)
async def register_client(response: Response,
                          registration_request: ClientRegistrationRequest,
                          authorization: Annotated[str | None, Header()] = None):
    if Policies.require_initial_token and not authorization:
        raise NoInitialTokenException
    response.status_code = 201
    return await process_registration(registration_request)


@router.get('/register',
            response_class=HTMLResponse)
async def get_client_register_form(request: Request):
    schema = ClientRegistrationRequest.model_json_schema(by_alias=True)
    return templates.TemplateResponse(request, name="client_reg.html", context={'properties': schema['properties'],
                                                                                'req': schema['required']})
