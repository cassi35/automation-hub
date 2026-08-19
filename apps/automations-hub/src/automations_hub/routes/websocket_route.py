from automations_hub.ConnectionManeger import ConnectionManager
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
websocket_router = APIRouter()
manager = ConnectionManager()
@websocket_router.websocket("/ws/executions")
async def execution_websocket(
    websocket: WebSocket,
):
    await manager.connect(websocket)

    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        manager.disconnect(websocket)