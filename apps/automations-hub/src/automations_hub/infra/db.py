from shared.db.settings.connection import BDConnectionHandler
database = BDConnectionHandler()
from rich import print
async def init_db()->BDConnectionHandler:
    print('[green]Initializing database...[/green]')
    with database as db:
        db.session.connection()
    return database