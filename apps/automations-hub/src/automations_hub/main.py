from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from rich import print
from automations_hub.sync_registry import sync_all_manifests
from automations_hub.infra.automation_repository import AutomationRepository
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[green]Starting up...[/green]")
    sync_all_manifests()
    automation = AutomationRepository().get_by_slug("english-news")
    if automation is not None:
        print(f"[green]{automation.slug.upper()}[/green] aqui é o slug")
    yield
    print("Shutting down...")

app = FastAPI(
    title="automations-hub",
    description="""
    O `orchestrator-api` é o **control plane** do `organize-tasks`: o serviço que sabe
    quais automações existem, qual o status de cada uma, o histórico de execuções,
    e consegue pausar/reativar cada uma — sem precisar entrar em cada automação
    individualmente pra saber o que está acontecendo.
    """,
    version="0.1.0",
    lifespan=lifespan,
)
@app.get("/")
async def root() -> dict:
    return {"message": "Hello from automations-hub!"}

def main() -> None:
    print(f"Hello from automations-hub!")
    uvicorn.run(
    "automations_hub.main:app", # precisa de uma string para dar reload
    host="0.0.0.0",
    port=8000,
    reload=True,
)
