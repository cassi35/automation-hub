import pytest
from rich import print
from apps.mcp_server.src.mcp_server.services.automation_service import (
    AutomationService,
)
from apps.mcp_server.src.mcp_server.services.execution_service import (
    ExecutionService,
)

@pytest.mark.skip(reason="This test is skipped because it requires a running database.")
@pytest.mark.mcp
def test_mcp_service():
    repo = AutomationService()
    automations = repo.get_all_automation()
    assert automations is not None
    assert len(automations) > 0

@pytest.mark.skip(reason="This test is skipped because it requires a running database.")

@pytest.mark.mcp
def test_get_by_slug():
    repo = AutomationService()
    automation = repo.get_automation_by_slug("jira-tasks")
    if automation is not None:
        assert automation.slug == "jira-tasks"
        print(f"[green]automation slug: {automation.slug} [/green]")


@pytest.mark.mcp
def test_get_all_executions_by_id():
    service = ExecutionService()
    executions = service.get_all_executions_by_id(1,1)
    assert executions is not None
    print(f"[green]Executions found for id 1: {len(executions)}[/green]")


@pytest.mark.mcp
def test_get_execution_by_status():
    service = ExecutionService()
    executions = service.get_execution_by_status("success",1)
    for execution in executions:
        print(f"[green]Execution ID: {execution.id}, Status: {execution.status}[/green]")
        assert execution.status == "success"

@pytest.mark.mcp
def test_get_error_message():
    service = ExecutionService()
    error_message = service.get_executions_by_error_message(1,1)
    print(f"[green]Error message for execution 1: {error_message}[/green]")