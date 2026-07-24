from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class StepStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"

@dataclass
class ExecutionStep:
    id: int | None
    execution_id: int
    name: str
    status: StepStatus
    started_at: datetime | None = None
    finished_at: datetime | None = None

    def start(self) -> None:
        self.status = StepStatus.RUNNING
        self.started_at = datetime.utcnow()

    def finish(self) -> None:
        self.status = StepStatus.SUCCESS
        self.finished_at = datetime.utcnow()

    def fail(self) -> None:
        self.status = StepStatus.FAILED
        self.finished_at = datetime.utcnow()