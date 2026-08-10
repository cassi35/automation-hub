from automations_hub.domain.steps import Step
from automations_hub.infra.execution_repository import ExecutionRepository


class StepService:
    def __init__(self):
        self._execution_repository = ExecutionRepository()

    def get_steps_by_execution_id(
        self,
        execution_id: int,
    ) -> list[Step]:
        return self._execution_repository.get_steps(execution_id)