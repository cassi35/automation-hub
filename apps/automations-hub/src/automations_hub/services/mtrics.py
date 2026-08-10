from automations_hub.domain.metrics import Metric
from automations_hub.infra.metrics_repository import MetricRepository


class MetricService:
    def __init__(self):
        self._metric_repository = MetricRepository()

    def get_metric_by_id(
        self,
        metric_id: int,
    ) -> Metric | None:
        return self._metric_repository.get_by_id(metric_id)

    def get_metrics_by_step_id(
        self,
        step_id: int,
    ) -> list[Metric]:
        return self._metric_repository.list_by_step_id(step_id)