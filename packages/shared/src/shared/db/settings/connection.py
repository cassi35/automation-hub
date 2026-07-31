from shared.config.config import Config
from sqlalchemy import create_engine,event
from sqlalchemy.orm import sessionmaker
from time import perf_counter
class BDConnectionHandler:
    def __init__(self, connection_string: str | None = None):
        self._connection_string = connection_string or Config.database_url_required

        self.__engine = create_engine(
            self._connection_string,
            echo=False,
            pool_size=5,
            pool_pre_ping=True,  # evita erro de conexão "morta" em serverless DB
        )
        print(self.__engine.dialect.driver)
        print(type(self.__engine.pool))
        print(self.__engine.dialect.driver)
        @event.listens_for(self.__engine, "checkout")
        def checkout(dbapi_connection, connection_record, connection_proxy):
            
            print(">>> CHECKOUT")

        @event.listens_for(self.__engine, "checkin")
        def checkin(dbapi_connection, connection_record):
            print("<<< CHECKIN")

        @event.listens_for(self.__engine, "before_cursor_execute")
        def before_execute(conn, cursor, statement, parameters, context, executemany):
            context._start = perf_counter()

        @event.listens_for(self.__engine, "after_cursor_execute")
        def after_execute(conn, cursor, statement, parameters, context, executemany):
            elapsed = perf_counter() - context._start
            print(f"{elapsed:.6f}s -> {statement.split()[0]}")
        self.__session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False,
        )

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        self.session = self.__session_factory()

        t = perf_counter()

        conn = self.session.connection()

        print(f"connection(): {perf_counter() - t:.3f}s")

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.session.rollback()
        else:
            t = perf_counter()
            self.session.commit()
            print(f"commit(): {perf_counter() - t:.6f}s")
        self.session.close()