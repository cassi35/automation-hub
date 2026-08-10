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

GitHub Actions
↓
pytest
↓
TestDatabaseHandler
↓

1. Testcontainer sobe PostgreSQL vazio
   ↓
2. obtém DATABASE_URL temporária
   ↓
3. Alembic usa ESSA URL temporária
   ↓
4. alembic upgrade head
   ↓
5. cria o schema no PostgreSQL temporário
   ↓
6. testes usam o mesmo banco
   ↓
7. container é destruído

# fluxo completo

```pytest
│
├── TestDatabaseHandler
│   │
│   ├── 1. Testcontainers sobe PostgreSQL
│   │
│   ├── 2. Obtém:
│   │      postgresql://test:...@localhost:random_port/test
│   │
│   ├── 3. Define temporariamente:
│   │      os.environ["DATABASE_URL"] = URL_DO_TESTCONTAINER
│   │
│   └── 4. Executa:
│          subprocess.run(["uv", "run", "alembic", "upgrade", "head"])
│
│
└── subprocesso do Alembic
    │
    ├── executa o Alembic
    │
    ├── importa seu env.py
    │
    ├── importa Config
    │
    ├── Config lê:
    │      DATABASE_URL=URL_DO_TESTCONTAINER
    │
    ├── aplica suas migrations
    │      48da8863abc3
    │      10e9cfc681a7
    │      b596510b37de
    │
    └── termina
```

depois

```
subprocess.run(...)
        ↓
Alembic executa
        ↓
alembic upgrade head termina
        ↓
subprocess termina
```

entao roda os testes no temporario

````PostgreSQL Testcontainer
        │
        ├── Alembic criou as tabelas
        │
        └── pytest testa:
            ├── INSERT
            ├── SELECT
            ├── UPDATE
            ├── DELETE
            └── relacionamentos
            ```
depois destroi

```

```pytest termina
↓
TestDatabaseHandler.close()
↓
engine.dispose()
↓
container.stop()
↓
PostgreSQL temporário destruído
```
````

sequencia real

```
# 1. Sobe banco temporário
container.start()

# 2. URL temporária
database_url = container.get_connection_url()

# 3. Sobrescreve o ambiente do processo de teste
os.environ["DATABASE_URL"] = database_url

# 4. Executa o Alembic
subprocess.run(
    ["uv", "run", "alembic", "upgrade", "head"],
    check=True,
)

# 5. Cria engine para o mesmo banco
engine = create_engine(database_url)

# 6. Testes usam esse banco
# pytest...

# 7. Ao final
engine.dispose()
container.stop()
```

# INFRA SHARED

                ExecutionTracker
                      │
                      ▼
                Queue[DBEvent]
                      │
                      ▼
            ThreadPoolExecutor
             /    /    \    \
            ▼    ▼      ▼    ▼
         worker worker worker worker
            \     \      /     /
             \     \    /     /
              └──── PostgreSQL
