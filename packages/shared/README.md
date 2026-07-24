# shared

nessa pasta vou fazer compartilhamento globais

# pastas

1. contracts/

- nessa pasta eu vou compratilhar contratos da db , execution.py e automation.py

## exemplo

```
packages/shared/
├── contracts/
│   ├── execution.py
│   └── automation.py
│
└── clients/
    └── orchestrator_client.py
```

```
class ExecutionStarted(BaseModel):
    execution_id: UUID
```

dai chama no english_news

```
execution = orchestrator_client.start_execution(
    automation="english-news"
)
```

2. clients/

- Um client é simplesmente um código que sabe conversar com outro sistema.

```
class OrchestratorClient:
    def start_execution(self, automation_name: str) -> int:
        ...  # cria linha em Execution, status=RUNNING, retorna execution_id

    def start_step(self, execution_id: int, name: str) -> int:
        ...  # cria linha em ExecutionStep, status=RUNNING

    def finish_step(self, step_id: int) -> None:
        ...  # status=SUCCESS

    def fail_step(self, step_id: int, error: str) -> None:
        ...  # status=FAILED

    def finish_execution(self, execution_id: int) -> None:
        ...

    def fail_execution(self, execution_id: int, error: str) -> None:
        ...
```

# registry

essa pasta tem um arquivo authmationMnyfest que é basicamente
um reggistro quando eu ligar o servidor
sincornizar

# fluxo
