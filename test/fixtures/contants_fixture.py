import pytest 
from shared.registry.manifest import AutomationManifest

@pytest.fixture()
def automation_manifest()-> AutomationManifest:
    return AutomationManifest(
        slug="jira-tasks",
        name="jira tyasks",
        description="Coleta notícias e gera tarefas no MS To-Do",
        trigger_type="github_actions",
        schedule="30 11 * * *",
    )