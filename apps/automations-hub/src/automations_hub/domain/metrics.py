from dataclasses import dataclass
from datetime import datetime


@dataclass
class Metric:
    id: int
    execution_at: datetime
    name: str
    value: int
    step_id: int