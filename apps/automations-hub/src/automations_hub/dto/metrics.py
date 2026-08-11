from datetime import datetime

from pydantic import BaseModel


class MetricResponse(BaseModel):
    id: int
    execution_at: datetime
    name: str
    value: int
    step_id: int