from fastapi import APIRouter, status

from automations_hub.dto.steps import StepResponse
from automations_hub.services.steps import StepService

step_router = APIRouter(tags=["steps"])

step_service = StepService()


@step_router.get(
    "/executions/{execution_id}/steps",
    response_model=list[StepResponse],
    status_code=status.HTTP_200_OK,
)
async def list_execution_steps(
    execution_id: int,
):
    """Lista os steps de uma execução."""
    return step_service.get_steps_by_execution_id(execution_id)