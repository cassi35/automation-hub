from test.confest import DatabaseTestHandler
from shared.config.config import Config
import pytest 
# def test_database_connection():
#     handler = DatabaseTestHandler()
#     engine = handler.get_engine()
#     print(f"aqui é o engine: {engine.url}")
#     print('\n')
#     print(f"aqui é o database_url_required: {Config.database_url_required}")
#     assert engine is not None
def test_database_connection():
    with DatabaseTestHandler() as handler:
        engine = handler.get_engine()
        print(f"Engine URL: {engine.url}")
        print(f"Config.DATABASE_URL: {Config.DATABASE_URL}")
        assert engine is not None