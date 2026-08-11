from shared.db.settings.connection import BDConnectionHandler
from rich import print

_database: BDConnectionHandler | None = None
def init_database(connection_string: str | None = None) -> None:
    global _database
    _database = BDConnectionHandler(connection_string)
# para chamar nos testes
def get_database() -> BDConnectionHandler:
    global _database
    if _database is None:
        _database = BDConnectionHandler()
    return _database

