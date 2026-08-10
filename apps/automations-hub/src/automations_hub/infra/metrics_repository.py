from automations_hub.domain.metrics import Metric
from automations_hub.infra.db import get_database
from shared.db.entities.automation import MetricModel
from shared.db.settings.connection import BDConnectionHandler


class MetricRepository:
    def __init__(self):
        self._db: BDConnectionHandler = get_database()

    def get_by_id(self, metric_id: int) -> Metric | None:
        with self._db as db:
            metric = (
                db.session
                .query(MetricModel)
                .filter_by(id=metric_id)
                .first()
            )

            if metric is None:
                return None

            return Metric(
                id=metric.id,
                execution_at=metric.execution_at,
                name=metric.name,
                value=metric.value,
                step_id=metric.step_id,
            )

    def list_by_step_id(self, step_id: int) -> list[Metric]:
        with self._db as db:
            metrics = (
                db.session
                .query(MetricModel)
                .filter_by(step_id=step_id)
                .all()
            )

            return [
                Metric(
                    id=metric.id,
                    execution_at=metric.execution_at,
                    name=metric.name,
                    value=metric.value,
                    step_id=metric.step_id,
                )
                for metric in metrics
            ]