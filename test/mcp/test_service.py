import pytest 
from  rich import print
from apps.mcp_server.src.mcp_server.services.automation_service import AutomationService
@pytest.mark.mcp
def test_mcp_service():
    repo = AutomationService()
    automations = repo.get_all_automation()
    assert automations is not None
    assert len(automations) > 0
@pytest.mark.mcp
def test_get_by_slug():
    repo = AutomationService()
    automation = repo.get_automation_by_slug("jira-tasks")
    if automation is not None:
        assert automation.slug == "jira-tasks"
        print(f"[green]automation slug: {automation.slug} [/green]")