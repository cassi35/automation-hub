from datetime import datetime

from pydantic import BaseModel, ConfigDict


class StepResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    status: str
    error_message: str | None


class ExecutionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    automation_id: int
    status: str
    start_at: datetime
    end_at: datetime | None
    error_message: str | None
    steps: list[StepResponse]


class ExecutionStepResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    status: str
    error_message: str | None