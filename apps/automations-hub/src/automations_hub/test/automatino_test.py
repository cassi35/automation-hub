import pytest
from automations_hub.infra.automation_repository import AutomationRepository
from shared.registry.manifest import AutomationManifest
from rich import print
# @pytest.mark.skip
def test_upsert_automation():

    manifest = AutomationManifest(
        slug="jira-tasks",
        name="jira tyasks",
        description="Coleta notícias e gera tarefas no MS To-Do",
        trigger_type="github_actions",
        schedule="30 11 * * *",
    )
    automation_repo = AutomationRepository()
    automation = automation_repo.upsert_automation(manifest)
    print(f"[green]{automation.name}[/green] aqui é o name")
def test_get_by_slug():
    automation_repo = AutomationRepository()
    automation = automation_repo.get_by_slug("jira-tasks")
    if automation is not None:
        print(f"[green]{automation.slug}[/green] aqui é o slug")