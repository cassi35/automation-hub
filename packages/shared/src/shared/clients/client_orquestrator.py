from datetime import datetime, timezone
from shared.db.settings.connection import BDConnectionHandler
from sqlalchemy import update
from shared.db.entities.automation import AutomationModel,ExecutionModel,MetricModel,StepModel
class OrchestratorClient:
    def __init__(self, connection_string: str | None = None):
        self._connection_string = connection_string
        self._handler = BDConnectionHandler(connection_string=connection_string)
        self._db: BDConnectionHandler | None = None

    def _require_db(self) -> BDConnectionHandler:
        if self._db is None:
            raise RuntimeError(
                "Sessão não iniciada. Chame start_execution() antes de qualquer outro método."
            )
        return self._db

    def start_execution(self, slug: str) -> int:
        self._db = self._handler.__enter__()  # abre a sessão UMA vez, fica viva até finish/fail

        automation = self._db.session.query(AutomationModel).filter_by(slug=slug).first()
        if automation is None:
            raise ValueError(f"Automation '{slug}' não encontrada")

        execution = ExecutionModel(
            automation_id=automation.id,
            status="process",
            start_at=datetime.now(timezone.utc),
        )
        self._db.session.add(execution)
        self._db.session.flush()
        self._db.session.commit()
        return execution.id

    def start_step(self, execution_id: int, name: str) -> int:
        db = self._require_db()
        step = StepModel(execution_id=execution_id, name=name, status="running")
        db.session.add(step)
        db.session.flush()
        db.session.commit()
        return step.id

    def finish_step(self, step_id: int) -> None:
        db = self._require_db()
        db.session.execute(
            update(StepModel).where(StepModel.id == step_id).values(status="stopped")
        )
        db.session.commit()

    def fail_step(self, step_id: int, error: str) -> None:
        db = self._require_db()
        step = db.session.get(StepModel, step_id)
        if step is None:
            raise ValueError(f"Step {step_id} não encontrado")
        step.status = "failed"
        step.error_message = error
        db.session.commit()

    def finish_execution(self, execution_id: int) -> None:
        db = self._require_db()
        db.session.execute(
            update(ExecutionModel)
            .where(ExecutionModel.id == execution_id)
            .values(status="success", end_at=datetime.now(timezone.utc))
        )
        db.session.commit()
        self._handler.__exit__(None, None, None)
        self._db = None

    def fail_execution(self, execution_id: int, error: str) -> None:
        db = self._require_db()
        execution = db.session.get(ExecutionModel, execution_id)
        if execution is None:
            raise ValueError(f"Execution {execution_id} não encontrada")
        execution.status = "failed"
        execution.error_message = error
        execution.end_at = datetime.now(timezone.utc)
        db.session.commit()
        self._handler.__exit__(None, None, None)
        self._db = None