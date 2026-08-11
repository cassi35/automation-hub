from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AutomationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    slug: str
    name: str
    trigger: str
    status: str


class ExecutionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    status: str
    start_at: datetime
    end_at: datetime | None
    error_message: str | None


class AutomationStatsResponse(BaseModel):
    success_rate: float
    average_duration: float
    total_executions: int


class TriggerAutomationResponse(BaseModel):
    message: str


class PauseAutomationResponse(BaseModel):
    message: str


class ResumeAutomationResponse(BaseModel):
    message: str