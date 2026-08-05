from automations_hub.dto.executionDto import (
    ExecutionResponse,
    ExecutionStepResponse,
)


class ExecutionService:
    async def get_execution_by_id(
        self,
        execution_id: int,
    ) -> ExecutionResponse:
        raise NotImplementedError()

    async def get_execution_steps(
        self,
        execution_id: int,
    ) -> list[ExecutionStepResponse]:
        raise NotImplementedError()

    async def get_all_executions_by_automation_id(
        self,
        automation_id: int,
    ) -> list[ExecutionResponse]:
        raise NotImplementedError()