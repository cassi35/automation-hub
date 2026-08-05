from shared.db.settings.connection import BDConnectionHandler
class ExecutionnRepository:
    def __init__(self,db:BDConnectionHandler):
        self._db = db