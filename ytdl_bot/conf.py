from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    
    TELEGRAM_TOKEN: str
    DATABASE_URL: str
    APP_NAME: str
    TELEGRAM_API_ID: int
    TELEGRAM_API_HASH: str


settings = Settings()