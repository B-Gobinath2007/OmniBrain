import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Base directory of the repository (parent of backend)
BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    APP_NAME: str = "OmniBrain API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    BACKEND_HOST: str = "0.0.0.0"
    BACKEND_PORT: int = 8000
    MAX_UPLOAD_SIZE_MB: int = 50
    MOCK_MODE: bool = True

    model_config = SettingsConfigDict(
        env_file=os.path.join(BASE_DIR, ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
