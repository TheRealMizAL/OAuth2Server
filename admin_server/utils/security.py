from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import jwt
from passlib.context import CryptContext

from .settings import get_settings, get_rsa_private, get_rsa_public

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth_scopes = {
    "openid": "Аутентификация OpenID Connect",
    "policies.all.get": "Получение всех политик безопасности",
    "policies.own.get": "Получение собственных политик безопасности",
    "policies.set": "Изменение всех политик безопасности",
}


def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)


def get_password_hash(plain):
    return pwd_context.hash(plain)


async def create_jwt(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(get_settings().default_jwt_exp)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, get_rsa_private(), algorithm=get_settings().jws_alg)


async def decode_jwt(token: str):
    return jwt.decode(token, get_rsa_public(), algorithms=get_settings().jws_alg)


class Policies:
    require_initial_token: bool = True

    def __init__(self, policies_server_ip: str):
        self.server_ip = policies_server_ip


policies = Policies('127.0.0.1:1488')
