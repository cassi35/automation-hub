from datetime import datetime
from shared.db.settings.connection import BDConnectionHandler
from shared.db.entities.automation import AutomationModel,ExecutionModel,MetricModel,StepModel
class OrchestratorClient:
    def start_execution(self, automation_name: str) -> int:
        # cria linha em Execution, status=RUNNING, retorna execution_id
        with BDConnectionHandler() as db:
            automation = db.session.query(AutomationModel).filter_by(name=automation_name).first()
            if automation is None:
                raise Exception("Automation not found")
            execution = ExecutionModel(
                automation_id=automation.id,
                status="process",
                start_at=datetime.utcnow(),
            )
            return execution.id
        ...
    def start_step(self, execution_id: int, name: str) -> int:
        # ...  # cria linha em ExecutionStep, status=RUNNING
        # with BDConnectionHandler() as db:
        #     pass
        ...
    def finish_step(self, step_id: int) -> None:
        ...  # status=SUCCESS
        # with BDConnectionHandler() as db:
        #     pass
    def fail_step(self, step_id: int, error: str) -> None:
        ...  # status=FAILED
        with BDConnectionHandler() as db:
            pass
    def finish_execution(self, execution_id: int) -> None:
        ...
        with BDConnectionHandler() as db:
            pass
    def fail_execution(self, execution_id: int, error: str) -> None:pass