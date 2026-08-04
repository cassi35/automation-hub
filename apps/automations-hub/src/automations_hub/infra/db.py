from rich import print

from shared.db.settings.connection import BDConnectionHandler


def get_database(connection_string: str | None = None) -> BDConnectionHandler:
    return BDConnectionHandler(connection_string=connection_string)


async def init_db() -> BDConnectionHandler:
    print("[green]Initializing database...[/green]")
    database = get_database()
    with database as db:
        db.session.connection()
    return database
