from contextlib import asynccontextmanager
from automations_hub.erros.exeptions import InvalidAutomationSlug
from automations_hub.erros.handlers import register_error_handlers
from automations_hub.infra.db import get_database
from fastapi import FastAPI
import uvicorn
from rich import print
from automations_hub.sync_registry import sync_all_manifests
from automations_hub.infra.automation_repository import AutomationRepository

from automations_hub.routes.automation_route import automation_router
from automations_hub.routes.execution_route import execution_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[green]Starting up...[/green]")
    get_database()
    sync_all_manifests()
    # registar erros 
    register_error_handlers(app)
    print()
    print('[blue]=========== application started SUCCESSFULLY =========== [/blue]')
    yield
    print("Shutting down...")

version = "0.1.0"
app = FastAPI(
    title="automations-hub",
    description="""
    O `orchestrator-api` é o **control plane** do `organize-tasks`: o serviço que sabe
    quais automações existem, qual o status de cada uma, o histórico de execuções,
    e consegue pausar/reativar cada uma — sem precisar entrar em cada automação
    individualmente pra saber o que está acontecendo.
    """,
    version=version,
    lifespan=lifespan,
)

# inclui rotas
app.include_router(automation_router, prefix=f"/api/{version}/automations", tags=["automations"])
app.include_router(automation_router, prefix="/automations", tags=["automations"])

app.include_router(execution_router, prefix=f"/api/{version}/executions", tags=["executions"])
app.include_router(execution_router, prefix="/executions", tags=["executions"])

# rotas princapis teste
@app.get("/")
async def root() -> dict:
    return {"message": "Hello from automations-hub!"}

@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}

@app.get("/test-error")
async def test_error() :
    raise InvalidAutomationSlug("test-error")

def main() -> None:
    print(f"Hello from automations-hub!")
    uvicorn.run(
        "automations_hub.main:app", # precisa de uma string para dar reload
        host="0.0.0.0",
        port=8000,
        reload=True,
    )

