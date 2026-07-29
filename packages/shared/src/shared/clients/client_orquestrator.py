from datetime import datetime, timezone
from shared.db.settings.connection import BDConnectionHandler
from shared.db.entities.automation import AutomationModel,ExecutionModel,MetricModel,StepModel
class OrchestratorClient:
    def __init__(self, connection_string: str | None = None):
        self._connection_string = connection_string
    def _db(self) -> BDConnectionHandler:
        return BDConnectionHandler(connection_string=self._connection_string)
    def start_execution(self, slug: str) -> int:
        with BDConnectionHandler() as db:
            automation = db.session.query(AutomationModel).filter_by(slug=slug).first()
            if automation is None:
                raise Exception("Automation not found")
            execution = ExecutionModel(
                automation_id=automation.id,
                status="process",
                start_at=datetime.now(timezone.utc),
            )
            db.session.add(execution)
            db.session.flush()   # gera o id sem precisar sair do "with" ainda
            return execution.id
    def start_step(self, execution_id: int, name: str) -> int:
        with BDConnectionHandler() as db:
            step = StepModel(
                execution_id=execution_id,
                name=name,
                status="running",
            )
            db.session.add(step)
            db.session.commit()
            return step.id
    def finish_step(self, step_id: int) -> None:
        with BDConnectionHandler() as db:
            step = db.session.get(StepModel, step_id)
            if step is None:
                raise ValueError(f"Step {step_id} não encontrado")
            step.status = "stopped"

    def fail_step(self, step_id: int, error: str) -> None:
        with BDConnectionHandler() as db:
            step = db.session.get(StepModel, step_id)
            if step is None:
                raise ValueError(f"Step {step_id} não encontrado")
            step.status = "failed"
            step.error_message = error

    def finish_execution(self, execution_id: int) -> None:
        with BDConnectionHandler() as db:
            execution = db.session.get(ExecutionModel, execution_id)
            if execution is None:
                raise ValueError(f"Execution {execution_id} não encontrada")
            execution.status = "success"
            execution.end_at = datetime.now(timezone.utc)

    def fail_execution(self, execution_id: int, error: str) -> None:
        with BDConnectionHandler() as db:
            execution = db.session.get(ExecutionModel, execution_id)
            if execution is None:
                raise ValueError(f"Execution {execution_id} não encontrada")
            execution.status = "failed"
            execution.error_message = error
            execution.end_at = datetime.now(timezone.utc)