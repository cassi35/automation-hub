import pytest
from shared.config.config import Config


@pytest.mark.integration
def test_database_connection(db_handler):
    """Testa a conexão com o banco de dados"""
    engine = db_handler.get_engine()
    print(f"Engine URL: {engine.url}")
    print(f"Config.DATABASE_URL: {Config.DATABASE_URL}")
    assert engine is not None