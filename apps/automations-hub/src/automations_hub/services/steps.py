from automations_hub.domain.steps import Step
from automations_hub.infra.execution_repository import ExecutionRepository


class StepService:
    def __init__(self):
        self._execution_repository = ExecutionRepository()

    def get_steps_by_execution_id(
        self,
        execution_id: int,
    ) -> list[Step]:
        steps =  self._execution_repository.get_steps(execution_id)

        return [
            Step(
                id=step.id,
                name=step.name,
                status=step.status,
                execution_id=step.execution_id
            )
            for step in steps
        ]