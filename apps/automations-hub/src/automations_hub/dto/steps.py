from pydantic import BaseModel


class StepResponse(BaseModel):
    id: int
    execution_id: int
    name: str
    status: str
    error_message: str | None = None