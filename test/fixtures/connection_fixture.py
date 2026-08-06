import pytest
from shared.db.settings.base import Base
from typing import Generator, Self
from sqlalchemy.orm import Session, sessionmaker
from test.conftest import DatabaseTestHandler
from automations_hub.infra.db import init_database
@pytest.fixture(scope="session")
def db_handler() -> Generator[DatabaseTestHandler, None, None]:
    with DatabaseTestHandler() as handler:
        init_database(handler.database_url)
        yield handler
@pytest.fixture
def automation_seed(db_handler) -> None:
    from automations_hub.sync_registry import sync_all_manifests
    sync_all_manifests()

@pytest.fixture
def db_session(db_handler) -> Generator[Session, None, None]:
    engine = db_handler.get_engine()

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    yield session

    session.close()
