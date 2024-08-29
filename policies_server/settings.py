from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=Path(__file__).parent / ".env")

    db_user: str
    db_pass: str
    db_host: str
    db_port: int
    db_name: str


__settings = Settings()

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
            "models": ["policies_server.main"],
            "default_connection": "default",
        },
    },
}
