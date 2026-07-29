from dataclasses import dataclass
from datetime import datetime

@dataclass
class Execution:
    id: int
    automation_id: int
    status: str
    started_at: datetime
    finished_at: datetime | None