from mcp_server.server import mcp
from mcp_server.services.automation_service import AutomationService
@mcp.tool(
        name="automation_list",
        description="List all automations",
)
def automation_list():
    automations = AutomationService().get_all_automation()
    return automations
@mcp.tool(name="automation_by_slug",description="Get automation by slug")
def automation_by_slug(slug:str):
    automation = AutomationService().get_automation_by_slug(slug)
    if automation == None or automation == []:
        return None
    return {
        "slug": automation.slug,
        "name": automation.name,
        "description": automation.description,
        "trigger":automation.trigger,
        "status": automation.status
    }