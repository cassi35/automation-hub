from dataclasses import dataclass


@dataclass
class ExecutionDTO:
    id: int
    automation_id: int
    status: str
    error_message: str | None
    start_at: str | None
    end_at: str | None