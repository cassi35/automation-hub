from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from automations_hub.services.execution_service import ExecutionService

execution_router = APIRouter(tags=["executions"])
execution_service = ExecutionService()


@execution_router.get("/{execution_id}", status_code=status.HTTP_200_OK)
async def get_execution_detail(execution_id: int):
    """Detalhe de uma execução (com steps)."""
    return await execution_service.get_execution_by_id(execution_id)


@execution_router.get("/{execution_id}/steps", status_code=status.HTTP_200_OK)
async def get_execution_steps(execution_id: int):
    """Só os steps dessa execução."""
    return await execution_service.get_execution_steps(execution_id)
