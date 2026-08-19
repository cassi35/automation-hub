import asyncio

from automations_hub.routes.websocket_route import manager


async def publish_execution_event(
    execution_id: int,
    event: str,
):
    await manager.broadcast({
        "type": event,
        "execution_id": execution_id,
    })