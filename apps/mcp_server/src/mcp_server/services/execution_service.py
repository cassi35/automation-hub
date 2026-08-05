from shared.db.settings.connection import BDConnectionHandler
from shared.db.entities.automation import ExecutionModel
from mcp_server.dto.execution import ExecutionDTO


class ExecutionService:
    def __init__(self):
        pass

    def get_all_executions_by_id(self, id: int,automation_id: int) -> list[ExecutionDTO]:
        with BDConnectionHandler() as db:
            executions = (
                db.session.query(ExecutionModel)
                .filter(
                    (ExecutionModel.automation_id == automation_id)
                    | (ExecutionModel.id == id)
                )
                .all()
            )
            return [
                ExecutionDTO(
                    id=e.id,
                    automation_id=e.automation_id,
                    status=e.status,
                    error_message=e.error_message,
                    start_at=e.start_at.isoformat() if e.start_at else None,
                    end_at=e.end_at.isoformat() if e.end_at else None,
                )
                for e in executions
            ]

    def get_execution_by_status(self, status: str,automation_id: int) -> list[ExecutionDTO]:
        with BDConnectionHandler() as db:
            executions = (
                db.session.query(ExecutionModel)
                .filter_by(status=status, automation_id=automation_id)
                .all()
            )
            return [
                ExecutionDTO(
                    id=e.id,
                    automation_id=e.automation_id,
                    status=e.status,
                    error_message=e.error_message,
                    start_at=e.start_at.isoformat() if e.start_at else None,
                    end_at=e.end_at.isoformat() if e.end_at else None,
                )
                for e in executions
            ]

    def get_executions_by_error_message(self, id: int, automation_id: int) -> str | None:
        with BDConnectionHandler() as db:
            execution = (
                db.session.query(ExecutionModel).filter_by(id=id, automation_id=automation_id).first()
            )
            if execution is None:
                return None
            return execution.error_message