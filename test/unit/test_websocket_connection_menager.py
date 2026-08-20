import time
import asyncio
import json
import pytest
from shared.clients.client_orquestrator import OrchestratorClient
import websockets

from automations_hub.routes.websocket_route import manager
from automations_hub.ConnectionManeger import ConnectionManager

@pytest.mark.asyncio
@pytest.mark.skip()
async def test_websocket_connection(server):
    
    async with websockets.connect(
        f"{server}/ws/executions"
    ):
        assert len(manager.connections) == 1

    assert len(manager.connections) == 0

def automation_fake(db_url:str):
    client =  OrchestratorClient(
        connection_string=db_url
    )
    execution_id = client.start_execution(
        "english-news"
    )
    step_id = client.start_step(
        execution_id,
        "scraping"
    )
    print("scraping")
    time.sleep(1)
    client.finish_step(step_id)
    client.finish_execution(execution_id)
    print("finalizando execucao")
@pytest.mark.asyncio
async def test_execution_realtime(
    server,
    db_handler,
):
    async with websockets.connect(
        f"{server}/ws/executions"
    ) as websocket:

        await asyncio.to_thread(
            automation_fake,
            db_handler.database_url,
        )

        message = await websocket.recv()

        data = json.loads(message)

        assert data["type"] == "execution.started"
