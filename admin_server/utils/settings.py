from functools import lru_cache
from pathlib import Path
from pydantic import UUID4

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=Path(__file__).parent / ".." / ".env")

    db_user: str
    db_pass: str
    db_host: str
    db_port: int
    db_name: str

    jws_alg: str = "RS256"
    default_jwt_exp: int = 30
    software_statement_exp_days: int = 3

    secret_key_path: str
    public_key_path: str

    client_id: UUID4


__settings = Settings()


@lru_cache()  # just to make dep injections easier
def get_settings() -> Settings:
    return __settings


@lru_cache()
def get_rsa_private() -> str:
    with open(get_settings().secret_key_path, encoding='utf-8') as f:
        return f.read()


@lru_cache()
def get_rsa_public() -> str:
    with open(get_settings().public_key_path, encoding='utf-8') as f:
        return f.read()


TORTOISE_ORM: dict = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": __settings.db_host,
                "port": __settings.db_port,
                "user": __settings.db_user,
                "password": __settings.db_pass,
                "database": __settings.db_name,
            }
        },
    },
    "apps": {
        "main": {
            "models": ["admin_server.models"],
            "default_connection": "default",
        },
    },
}
