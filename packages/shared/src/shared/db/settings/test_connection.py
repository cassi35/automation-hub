from shared.db.settings.connection import BDConnectionHandler
import pytest
def test_create_db_engine():
    db_connection_handler = BDConnectionHandler()
    engine = db_connection_handler.get_engine()
    print(engine)
    
    assert engine is not  None