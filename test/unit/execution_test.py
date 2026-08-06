from automations_hub.infra.execution_repository import ExecutionRepository
from automations_hub.infra.automation_repository import AutomationRepository
from automations_hub.infra.db import init_database

repo_execution = ExecutionRepository()
automation_repo = AutomationRepository()
def test_get_by_id(automation_manifest):
    pass