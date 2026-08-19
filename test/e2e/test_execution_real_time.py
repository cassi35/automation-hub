from fastapi.testclient import TestClient
import pytest
import pytest
import asyncio
import websockets
@pytest.mark.e2e
def test_websocket_connection(server):
    async def run():
        async with websockets.connect(
            f"{server}/ws/events"
        ) as websocket:

            await websocket.send("ping")

    asyncio.run(run())