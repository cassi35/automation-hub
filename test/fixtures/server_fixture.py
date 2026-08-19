import threading
import time

import pytest
import uvicorn

from automations_hub.main import app

@pytest.fixture(scope="session")
def server(db_handler):
    config = uvicorn.Config(
        app,
        host="127.0.0.1",
        port=8001,
        log_level="error",
    )

    server = uvicorn.Server(config)

    thread = threading.Thread(
        target=server.run,
        daemon=True,
    )

    thread.start()

    while not server.started:
        time.sleep(0.01)

    yield "ws://127.0.0.1:8001/api/0.1.0"

    server.should_exit = True
    thread.join()