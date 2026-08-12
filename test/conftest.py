from typing import  Self
from types import TracebackType
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from testcontainers.community.postgres import PostgresContainer
from shared.config.config import Config
import os
import subprocess
from pathlib import Path

def find_root(marker: str = ".git") -> Path:
    path = Path(__file__).resolve()
    for parent in path.parents:
        if (parent / marker).exists():
            return parent
    raise FileNotFoundError(f"Não achei {marker} subindo a partir de {path}")


AUTOMATIONS_HUB_DIR = Path(__file__).resolve().parent.parent / "apps" / "automations-hub"

class DatabaseTestHandler:
    def __init__(self) -> None:
        self.container = PostgresContainer(
            "postgres:16",
            username="test",
            password="test",
            dbname="test",
        )

    def start(self) -> Self:
        self.container.start()
        self.database_url = self.container.get_connection_url()

        os.environ["DATABASE_URL"] = self.database_url
        Config.DATABASE_URL = self.database_url

        self._run_migrations()
        self.engine = create_engine(self.database_url)
        return self

    def _run_migrations(self) -> None:
        subprocess.run(
            ["uv", "run", "alembic", "upgrade", "head"],
            check=True,
            cwd=AUTOMATIONS_HUB_DIR,
        )

    def get_engine(self) -> Engine:
        return self.engine

    def close(self) -> None:
        if hasattr(self, "engine"):
            self.engine.dispose()
        self.container.stop()

    # Métodos exigidos pelo Pylance para validar a sintaxe 'with'
    def __enter__(self) -> Self:
        return self.start()

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.close()

pytest_plugins = [
    "test.fixtures.connection_fixture",
    "test.fixtures.fixture_models",
    "test.fixtures.repositories_fixtures",
    "test.fixtures.contants_fixture",
]