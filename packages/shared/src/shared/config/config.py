from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from pathlib import Path
from pydantic import Field
def find_root(marker: str = ".git") -> Path:
    path = Path(__file__).resolve()
    for parent in path.parents:
        if (parent / marker).exists():
            return parent
    raise FileNotFoundError(f"Não achei {marker} subindo a partir de {path}")

ROOT_DIR = find_root()
class Settings(BaseSettings):
    JIRA_TKOEN: str | None = None
    MICROSOFT_GRAPH:  str | None = None
    DATABASE_URL:  str | None = None

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
    @property
    def database_url_required(self) -> str:
        if self.DATABASE_URL is None:
            raise RuntimeError(
                "DATABASE_URL não configurada. Verifique o .env na raiz do projeto."
            )
        return self.DATABASE_URL

Config = Settings()
print(Config.DATABASE_URL)