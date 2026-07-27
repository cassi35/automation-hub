# import os
# import subprocess
# from pathlib import Path

# from sqlalchemy import create_engine
# from sqlalchemy.engine import Engine
# from testcontainers.community.postgres import PostgresContainer

# AUTOMATIONS_HUB_DIR = Path(__file__).resolve().parent.parent / "apps" / "automations-hub"
# import pytest

# class DatabaseTestHandler:
#     def __init__(self):
#         __test__ = False
#         self.container = PostgresContainer(
#             "postgres:16",
#             username="test",
#             password="test",
#             dbname="test",
#         )

#         self.container.start()

#         self.database_url = self.container.get_connection_url()

#         os.environ["DATABASE_URL"] = self.database_url

#         self._run_migrations()

#         self.engine = create_engine(self.database_url)

#     def _run_migrations(self):
#         subprocess.run(
#             ["uv", "run", "alembic", "upgrade", "head"],
#             check=True,
#             cwd=AUTOMATIONS_HUB_DIR,   # <- roda o comando de dentro dessa pasta
#         )

#     def get_engine(self) -> Engine:
#         return self.engine

#     def close(self):
#         self.engine.dispose()
#         self.container.stop()
# @pytest.fixture(scope="session", autouse=True)
# def db_handler():
#     with DatabaseTestHandler() as handler:
#         yield handler
from typing import Generator, Self
from types import TracebackType
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker
from testcontainers.community.postgres import PostgresContainer
from shared.config.config import Config
import os
import subprocess
from pathlib import Path
import pytest
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

@pytest.fixture(scope="session")
def db_handler() -> Generator[DatabaseTestHandler, None, None]:
    with DatabaseTestHandler() as handler:
        yield handler


@pytest.fixture
def db_session(db_handler: DatabaseTestHandler) -> Generator[Session, None, None]:
    SessionLocal = sessionmaker(bind=db_handler.get_engine())
    session = SessionLocal()
    yield session
    session.rollback()
    session.close()