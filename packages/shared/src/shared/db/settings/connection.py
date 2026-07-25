from shared.config.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
class BDConnectionHandler:
    def __init__(self):
        self._connection_string = Config.database_url_required

        self.__engine = create_engine(
            self._connection_string,
            echo=True,
        )

        self.__session_factory = sessionmaker(
            bind=self.__engine,
        )

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        self.session = self.__session_factory()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()

        self.session.close()