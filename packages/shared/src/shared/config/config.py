from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from pathlib import Path
from pydantic import Field, ValidationError
from rich import print
def find_root(marker: str = ".git") -> Path:
    path = Path(__file__).resolve()
    for parent in path.parents:
        if (parent / marker).exists():
            return parent
    raise FileNotFoundError(f"Não achei {marker} subindo a partir de {path}")

ROOT_DIR = find_root()
class Settings(BaseSettings):
    JIRA_TKOEN: str=Field(min_length=1)
    MICROSOFT_GRAPH:  str =Field(min_length=1)
    DATABASE_URL:  str | None = Field(min_length=1)
    REACT_URL: str = Field(min_length=1)
    AUTOMATION_HUB:  str | None = None
    GROQ_API:str = Field(min_length=1)
    GOOGLE_STDIO_API:str = Field(min_length=1)
    LLM_MODEL:str = Field(min_length=1)
    LLM_MODEL_GROQ:str = Field(min_length=1)
    LLM_MODEL_GOOGLE:str = Field(min_length=1)
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

    def __init__(self) -> None:
        super().__init__()
try:
    Config = Settings()
except ValidationError as exc:
    for error in exc.errors():
        field = ".".join(str(x) for x in error["loc"])
        print(f" [red] ERRO:[/red][blue]{field}[/blue] {error['msg']}")

    raise SystemExit(1)