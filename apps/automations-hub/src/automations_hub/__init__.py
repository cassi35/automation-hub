from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
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
    print("Hello from automations-hub!")
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()