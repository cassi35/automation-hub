from automations_hub.domain.metrics import Metric
from automations_hub.infra.metrics_repository import MetricRepository
from automations_hub.dto.metrics import MetricResponse
class MetricService:
    def __init__(self):
        self._metric_repository = MetricRepository()

    def get_metric_by_id(
        self,
        metric_id: int,
    ) -> MetricResponse | None:
        metric = self._metric_repository.get_by_id(metric_id)

        if metric is None:
            raise Exception("Metric not found")

        return MetricResponse(
            id=metric.id,
            execution_at=metric.execution_at,
            name=metric.name,
            value=metric.value,
            step_id=metric.step_id,
        )
    def get_metrics_by_step_id(
        self,
        step_id: int,
    ) -> list[MetricResponse]:
        metrics = self._metric_repository.list_by_step_id(step_id)

        return [
            MetricResponse(
                id=metric.id,
                execution_at=metric.execution_at,
                name=metric.name,
                value=metric.value,
                step_id=metric.step_id,
            )
            for metric in metrics
        ]