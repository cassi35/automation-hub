import asyncio
import json
import select
import threading

import psycopg2

from automations_hub.routes.websocket_route import manager


class ExecutionEventListener:

    def __init__(
        self,
        database_url: str,
        loop: asyncio.AbstractEventLoop,
    ):
        self.database_url = database_url
        self.loop = loop
        self._stop_event = threading.Event()
        self._thread: threading.Thread | None = None

    def start(self):
        self._thread = threading.Thread(
            target=self._listen,
            daemon=True,
        )
        self._thread.start()

    def stop(self):
        self._stop_event.set()

        if self._thread:
            self._thread.join(timeout=2)

    def _listen(self):
        try:
            connection = psycopg2.connect(
                self.database_url.replace(
                    "postgresql+psycopg2://",
                    "postgresql://",
                    1,
                )
            )

            connection.set_isolation_level(
                psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
            )

            cursor = connection.cursor()

            cursor.execute("LISTEN execution_events;")

            print("LISTEN execution_events conectado")

            while not self._stop_event.is_set():

                readable, _, _ = select.select(
                    [connection],
                    [],
                    [],
                    1,
                )

                if not readable:
                    continue

                connection.poll()

                while connection.notifies:
                    notification = connection.notifies.pop(0)

                    print(
                        "NOTIFY RECEBIDO:",
                        notification.payload,
                    )

                    message = json.loads(
                        notification.payload
                    )

                    asyncio.run_coroutine_threadsafe(
                        manager.broadcast(message),
                        self.loop,
                    )

            cursor.close()
            connection.close()

        except Exception as e:
            print(
                f"ERRO NO EXECUTION LISTENER: {e}"
            )