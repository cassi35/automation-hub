from automations_hub.dto.automationDto import (
    AutomationResponse,
    AutomationStatsResponse,
    ExecutionResponse,
    PauseAutomationResponse,
    PauseAutomationResponse,
    TriggerAutomationResponse,
)
from automations_hub.infra.automation_repository import AutomationRepository
from automations_hub.infra.execution_repository import ExecutionRepository
class AutomationService:
    def __init__(self):
        self._automation_repository = AutomationRepository()
        self._execution_repository = ExecutionRepository()
    async def get_all_automations(
        self,
    ) -> list[AutomationResponse]:
        raise NotImplementedError()

    async def get_automation_by_slug(
        self,
        slug: str,
    ) -> AutomationResponse:
        raise NotImplementedError()

    async def pause_automation(
        self,
        slug: str,
    ) -> PauseAutomationResponse:
        raise NotImplementedError()

    async def resume_automation(
        self,
        slug: str,
    ) -> PauseAutomationResponse:
        raise NotImplementedError()

    async def trigger_automation(
        self,
        slug: str,
    ) -> TriggerAutomationResponse:
        raise NotImplementedError()

    async def get_executions_by_automation_slug(
        self,
        slug: str,
    ) -> list[ExecutionResponse]:
        raise NotImplementedError()

    async def get_automation_stats(
        self,
        slug: str,
    ) -> AutomationStatsResponse:
        raise NotImplementedError()