import pytest
from automations_hub.infra.execution_repository import ExecutionRepository
from automations_hub.infra.automation_repository import AutomationRepository
from automations_hub.infra.db import init_database
# iniciar a db com testscontainer 
@pytest.fixture()
def repo_execution() -> ExecutionRepository:
    return ExecutionRepository()
@pytest.fixture()
def automation_repo() -> AutomationRepository:
    return AutomationRepository()