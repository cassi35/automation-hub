from automations_hub.domain.execution import Execution
from automations_hub.domain.steps import Step
from automations_hub.infra.db import get_database
from shared.db.entities.automation import AutomationModel, ExecutionModel, StepModel
from shared.db.settings.connection import BDConnectionHandler


class ExecutionRepository:
    def __init__(self):
        self._db: BDConnectionHandler = get_database()

    def get_by_execution_id(self, execution_id: int) -> Execution | None:
        with self._db as db:
            db.session.query(ExecutionModel).filter_by(id=execution_id).first()
            execution = db.session.query(ExecutionModel).filter_by(id=execution_id).first()
            if execution is None:
                return None

            return Execution(
                id=execution.id,
                automation_id=execution.automation_id,
                status=execution.status,
                started_at=execution.start_at,
                finished_at=execution.end_at,
            )

    def list_by_automation_id(self, automation_id: int) -> list[Execution] | None:
        with self._db as db:
            automation = db.session.query(AutomationModel).filter_by(id=automation_id).first()

            if automation is None:
                return None

            executions = (
                db.session.query(ExecutionModel)
                .filter_by(automation_id=automation_id)
                .all()
            )

            return [
                Execution(
                    id=execution.id,
                    automation_id=execution.automation_id,
                    status=execution.status,
                    started_at=execution.start_at,
                    finished_at=execution.end_at,
                )
                for execution in executions
            ]

    def get_steps(self, execution_id: int) -> list[Step]:
        with self._db as db:
            steps = db.session.query(StepModel).filter_by(execution_id=execution_id).all()

            return [
                Step(
                    id=step.id,
                    execution_id=step.execution_id,
                    name=step.name,
                    status=step.status,
                )
                for step in steps
            ]

    def get_by_automation_id(self, automation_id: int):
        with self._db as db:
            execution = (
                db.session.query(ExecutionModel).filter_by(automation_id=automation_id).first()
            )

            if execution is None:
                return None

            return Execution(
                id=execution.id,
                automation_id=execution.automation_id,
                status=execution.status,
                started_at=execution.start_at,
                finished_at=execution.end_at,
            )

    def get_executions_by_slug(self, slug: str) -> list[Execution]:
        with self._db as db:
            automation = db.session.query(AutomationModel).filter_by(slug=slug).first()

            if automation is None:
                return []

            executions = (
                db.session.query(ExecutionModel)
                .filter_by(automation_id=automation.id)
                .all()
            )

            return [
                Execution(
                    id=execution.id,
                    automation_id=execution.automation_id,
                    status=execution.status,
                    started_at=execution.start_at,
                    finished_at=execution.end_at,
                )
                for execution in executions
            ]
