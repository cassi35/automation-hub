import asyncio
import json
import select
import threading
import time

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
        while not self._stop_event.is_set():
            connection = None

            try:
                connection = psycopg2.connect(
                    self.database_url
                )

                connection.set_isolation_level(
                    psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
                )

                cursor = connection.cursor()

                cursor.execute(
                    "LISTEN execution_events;"
                )

                print(
                    "LISTEN execution_events conectado"
                )

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
                        notification = (
                            connection.notifies.pop(0)
                        )

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

            except Exception as e:
                if not self._stop_event.is_set():
                    print(
                        f"Execution listener disconnected: {e}"
                    )

                    time.sleep(2)

            finally:
                if connection is not None:
                    try:
                        connection.close()
                    except Exception:
                        pass