from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Configuration for the settings model
    model_config = SettingsConfigDict(
        extra="allow",  # Allow extra fields in the environment variables
        env_ignore_empty=False,  # Do not ignore empty environment variables
        env_file=".env"  # Specify the environment file to load
    ) 
    
    # Application settings with default values
    HOST: Optional[str] = "127.0.0.1"  # Default host address
    PORT: Optional[int] = 8000  # Default port number
    LOG_FILE_PATH: Optional[str] = "logs/app.log"  # Default log file path