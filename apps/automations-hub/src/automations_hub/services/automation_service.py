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
        automations = self._automation_repository.get_all_automations()
        if not automations:
            raise ValueError("no automations found")
        automations_response = [
            AutomationResponse(
                id=automation.id,
                slug=automation.slug,
                name=automation.name,
                trigger=automation.trigger_type,
                status=automation.status,
            )
            for automation in automations
        ]
        return automations_response

    async def get_automation_by_slug(
        self,
        slug: str,
    ) -> AutomationResponse:
        self.error_slug(slug)
        automation = self._automation_repository.get_by_slug(slug)
        if automation is None or automation == []:
            raise ValueError("automation not found")
        automation_response = AutomationResponse(
            id=automation.id,
            slug=automation.slug,
            name=automation.name,
            trigger=automation.trigger_type,
            status=automation.status,
        )
        return automation_response

    async def pause_automation(
        self,
        slug: str,
    ) -> PauseAutomationResponse:
        self.error_slug(slug)
        
        raise NotImplementedError()

    async def resume_automation(
        self,
        slug: str,
    ) -> PauseAutomationResponse:
        self.error_slug(slug)
        
        raise NotImplementedError()

    async def trigger_automations(
        self,
        trigger: str,
    ) -> TriggerAutomationResponse:
        if trigger is None or trigger == "" or (trigger != "github_actions" or trigger != "system"):
            raise ValueError("trigger must be github_actions or system")
        automations = self._automation_repository.get_all_automations_by_trigger(trigger)
        return automations

    async def get_executions_by_automation_slug(
        self,
        slug: str,
    ) -> list[ExecutionResponse]:
        self.error_slug(slug)
        automation = self._automation_repository.get_by_slug(slug)
        if automation is None or automation == []:
            raise ValueError("automation not found")
        executions = self._execution_repository.get_executions_by_slug(slug)

        executions_response = [
            ExecutionResponse(
                end_at=execution.finished_at,
                start_at=execution.started_at,
                status=execution.status,
                id=execution.id,
                error_message=None,
            )
            for execution in executions
        ]
        return executions_response

    async def get_automation_stats(
        self,
        slug: str,
    ) -> AutomationStatsResponse:
        
        self.error_slug(slug)
        self.error_slug(slug)

        executions = self._execution_repository.get_executions_by_slug(slug)

        total_executions = len(executions)

        if total_executions == 0:
            return AutomationStatsResponse(
                success_rate=0.0,
                average_duration=0.0,
                total_executions=0,
            )

        successful_executions = [
            execution
            for execution in executions
            if execution.status == "success"
        ]

        completed_executions = [
            execution
            for execution in executions
            if execution.started_at is not None
            and execution.finished_at is not None
        ]
        durations = [
            (execution.finished_at - execution.started_at).total_seconds()
            for execution in executions
            if execution.finished_at is not None
            and execution.started_at is not None
        ]

        success_rate = (
            len(successful_executions) / total_executions
        ) * 100

        average_duration = (
            sum(durations) / len(durations)
            if durations
            else 0.0
        )

        return AutomationStatsResponse(
            success_rate=success_rate,
            average_duration=average_duration,
            total_executions=total_executions,
        )
    def error_slug(self,slug:str):
        if len(slug) == 0 or slug is None :
             raise ValueError("slug is required")
        if not isinstance(slug,str):
            raise ValueError("slug must be a string")
