from functools import lru_cache
from pathlib import Path

from pydantic import UUID4
from pydantic_settings import BaseSettings, SettingsConfigDict

from .schemas import HttpsUrl


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=Path(__file__).parent / ".env", extra='ignore')

    auth_server_address: HttpsUrl

    jws_alg: str = "RS256"
    default_jwt_exp: int = 30
    software_statement_exp_days: int = 3

    client_id: str = 'aboba'
    required_scopes: str = 'openid'


__settings = Settings()


@lru_cache()  # just to make dep injections easier
def get_settings() -> Settings:
    return __settings
