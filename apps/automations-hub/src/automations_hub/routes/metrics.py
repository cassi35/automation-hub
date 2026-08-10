from fastapi import APIRouter, status

from automations_hub.dto.metrics import MetricResponse
from automations_hub.services.mtrics import MetricService

metric_router = APIRouter(tags=["metrics"])

metric_service = MetricService()


@metric_router.get(
    "/steps/{step_id}/metrics",
    response_model=list[MetricResponse],
    status_code=status.HTTP_200_OK,
)
async def list_step_metrics(
    step_id: int,
):
    """Lista as métricas de um step."""
    return metric_service.get_metrics_by_step_id(step_id)


@metric_router.get(
    "/metrics/{metric_id}",
    response_model=MetricResponse,
    status_code=status.HTTP_200_OK,
)
async def get_metric(
    metric_id: int,
):
    """Retorna uma métrica."""
    return metric_service.get_metric_by_id(metric_id)