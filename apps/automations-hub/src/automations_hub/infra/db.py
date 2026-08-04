from shared.db.settings.connection import BDConnectionHandler
from rich import print
database = BDConnectionHandler()
async def init_db()->BDConnectionHandler:
    print('[green]Initializing database...[/green]')
    with database as db:
        db.session.connection()
    return database