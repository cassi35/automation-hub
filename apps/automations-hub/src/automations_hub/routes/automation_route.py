from fastapi import APIRouter, status, BackgroundTasks

from automations_hub.dto.automationDto import (
    AutomationResponse,
    AutomationStatsResponse,
    ExecutionResponse,
    PauseAutomationResponse,
    TriggerAutomationResponse,
)
from automations_hub.services.automation_service import AutomationService

automation_router = APIRouter(tags=["automations"])

automation_service = AutomationService()

@automation_router.get(
    "/",
    response_model=list[AutomationResponse],
    status_code=status.HTTP_200_OK,
    operation_id="list_automations",
)
async def list_automations():
    """Lista todas as automações."""
    return await automation_service.get_all_automations()


@automation_router.get(
    "/{slug}",
    response_model=AutomationResponse,
    status_code=status.HTTP_200_OK,
    operation_id="get_automation_detail",
)
async def get_automation_detail(slug: str):
    """Detalhe de uma automação pelo slug."""
    return await automation_service.get_automation_by_slug(slug)


@automation_router.patch(
    "/{slug}/pause",
    response_model=PauseAutomationResponse,
    status_code=status.HTTP_200_OK,
    operation_id="pause_automation",
)
async def pause_automation(slug: str):
    """Pausa uma automação."""
    return await automation_service.pause_automation(slug)


@automation_router.patch(
    "/{slug}/resume",
    response_model=PauseAutomationResponse,
    status_code=status.HTTP_200_OK,
    operation_id="resume_automation",
)
async def resume_automation(slug: str):
    """Retoma uma automação."""
    return await automation_service.resume_automation(slug)


@automation_router.post(
    "/{slug}/trigger",
    response_model=TriggerAutomationResponse,
    status_code=status.HTTP_200_OK,
    operation_id="trigger_automation",
)
async def trigger_automation(slug: str, background_tasks: BackgroundTasks):
    """Dispara execução manual de uma automação."""
    return await automation_service.get_executions_by_automation_slug(slug)


@automation_router.get(
    "/{slug}/executions",
    response_model=list[ExecutionResponse],
    status_code=status.HTTP_200_OK,
    operation_id="list_automation_executions",
)
async def list_automation_executions(slug: str):
    """Histórico de execuções dessa automação."""
    return await automation_service.get_executions_by_automation_slug(slug)


@automation_router.get(
    "/{slug}/stats",
    response_model=AutomationStatsResponse,
    status_code=status.HTTP_200_OK,
    operation_id="get_automation_stats",
)
async def get_automation_stats(slug: str):
    """Taxa de sucesso e duração média da automação."""
    return await automation_service.get_automation_stats(slug)
