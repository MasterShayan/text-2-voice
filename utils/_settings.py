from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="allow",
        env_ignore_empty=False,
        env_file=".env"
    ) 
    

    HOST: Optional[str] = "127.0.0.1"
    PORT: Optional[int] = 8000
    LOG_FILE_PATH: Optional[str] = "logs/app.log"