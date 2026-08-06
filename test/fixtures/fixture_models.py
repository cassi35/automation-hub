import pytest

from shared.db.entities.automation import AutomationModel, ExecutionModel, MetricModel, StepModel


@pytest.fixture()
def automation_model() -> AutomationModel:
    return AutomationModel(
        name="deploy-prod",
        trigger="github_actions",
        status="active",
        slug="deploy-prod",
    )


@pytest.fixture()
def execution_model(automation_model: AutomationModel) -> ExecutionModel:
    return ExecutionModel(
        status="process",
        automation=automation_model,
    )


@pytest.fixture()
def step_model(execution_model: ExecutionModel) -> StepModel:
    return StepModel(
        name="build",
        status="running",
        execution=execution_model,
    )


@pytest.fixture()
def metric_model(step_model: StepModel) -> MetricModel:
    return MetricModel(
        name="duration",
        value=120,
        step=step_model,
    )
