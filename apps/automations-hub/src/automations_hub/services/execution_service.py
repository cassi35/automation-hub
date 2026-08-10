from automations_hub.dto.executionDto import (
    ExecutionResponse,
    ExecutionStepResponse,
)
from automations_hub.dto.executionDto import StepResponse
from automations_hub.infra.automation_repository import AutomationRepository
from automations_hub.infra.execution_repository import ExecutionRepository
class ExecutionService:
    def __init__(self):
        self.execution_repo = ExecutionRepository()
        self.automation_repo = AutomationRepository()
    async def get_execution_by_id(
        self,
        execution_id: int,
    ) -> ExecutionResponse:

        if execution_id is None:
            raise ValueError("execution_id is required")

        execution = self.execution_repo.get_by_execution_id(execution_id)

        if execution is None:
            raise ValueError("execution not found")

        steps = self.execution_repo.get_steps(execution_id)

        execution_response = ExecutionResponse(
            id=execution.id,
            automation_id=execution.automation_id,
            status=execution.status,
            start_at=execution.started_at,
            end_at=execution.finished_at,
            error_message=None,
            steps=[
                StepResponse(
                    id=step.id,
                    name=step.name,
                    status=step.status,
                    error_message=None,
                )
                for step in steps
            ],
        )

        return execution_response
    async def get_execution_steps(
        self,
        execution_id: int,
    ) -> list[StepResponse]:
        steps = self.execution_repo.get_steps(execution_id)
        return [
                StepResponse(
                    id=step.id,
                    name=step.name,
                    status=step.status,
                    error_message=None,
                )
                for step in steps
            ]

    async def get_all_executions_by_automation_id(
        self,
        automation_id: int,
    ) -> list[ExecutionResponse]:
        executions_all = self.execution_repo.list_by_automation_id(automation_id)
        if executions_all == [] or executions_all is None:
            return []
        executions = [ExecutionResponse(
            id=execution.id,
            automation_id=execution.automation_id,
            status=execution.status,
            start_at=execution.started_at,
            end_at=execution.finished_at,
            error_message=None,
            steps=[]
        ) for execution in executions_all]
        return executions