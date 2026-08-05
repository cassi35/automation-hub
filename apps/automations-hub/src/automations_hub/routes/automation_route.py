from fastapi import APIRouter, Depends, status, BackgroundTasks
from fastapi.responses import JSONResponse
from automations_hub.services.automation_service import AutomationService

automation_router = APIRouter(tags=["automations"])
automation_service = AutomationService()


@automation_router.get("", status_code=status.HTTP_200_OK)
@automation_router.get("/", status_code=status.HTTP_200_OK)
async def list_automations():
    """Lista todas as automações."""
    return await automation_service.get_all_automations()


@automation_router.get("/{slug}", status_code=status.HTTP_200_OK)
async def get_automation_detail(slug: str):
    """Detalhe de uma automação pelo slug."""
    return await automation_service.get_automation_by_slug(slug)


@automation_router.patch("/{slug}/pause", status_code=status.HTTP_200_OK)
async def pause_automation(slug: str):
    """Pausa uma automação."""
    return await automation_service.pause_automation(slug)


@automation_router.patch("/{slug}/resume", status_code=status.HTTP_200_OK)
async def resume_automation(slug: str):
    """Retoma uma automação."""
    return await automation_service.resume_automation(slug)


@automation_router.post("/{slug}/trigger", status_code=status.HTTP_200_OK)
async def trigger_automation(slug: str, background_tasks: BackgroundTasks):
    """Dispara execução manual de uma automação."""
    return await automation_service.trigger_automation(slug)


@automation_router.get("/{slug}/executions", status_code=status.HTTP_200_OK)
async def list_automation_executions(slug: str):
    """Histórico de execuções dessa automação."""
    return await automation_service.get_executions_by_automation_slug(slug)


@automation_router.get("/{slug}/stats", status_code=status.HTTP_200_OK)
async def get_automation_stats(slug: str):
    """Taxa de sucesso e duração média da automação."""
    return await automation_service.get_automation_stats(slug)
