from shared.db.settings.connection import BDConnectionHandler
from rich import print

_database: BDConnectionHandler | None = None

def get_database() -> BDConnectionHandler:
    global _database
    if _database is None:
        _database = BDConnectionHandler()
    return _database

async def init_db() -> BDConnectionHandler:
    db = get_database()
    print('[green]Initializing database...[/green]')
    with db as conn:
        conn.session.connection()
    return db