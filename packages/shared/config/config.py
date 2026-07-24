from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parents[3]
class Settings(BaseSettings):
    JIRA_TKOEN: str | None = None
    MICROSOFT_GRAPH:  str | None = None
    DATABASE_URL:  str | None = None

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


Config = Settings()
