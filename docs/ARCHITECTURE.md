# flow systeam

```

sequenceDiagram
    participant Trigger as GitHub Actions / systemd
    participant Auto as packages/english-news
    participant Client as OrchestratorClient (shared)
    participant DB as Postgres (Neon)
    participant API as automations-hub (API)
    participant FE as Frontend (React)

    Trigger->>Auto: executa main.py
    Auto->>Client: start_execution("english-news")
    Client->>DB: INSERT INTO executions (status=RUNNING)
    DB-->>Client: execution_id

    Auto->>Client: start_step(execution_id, "scraping")
    Client->>DB: INSERT INTO execution_steps (status=RUNNING)
    DB-->>Client: step_id
    Auto->>Auto: scrape_sources()
    Auto->>Client: finish_step(step_id)
    Client->>DB: UPDATE execution_steps SET status=SUCCESS

    Auto->>Client: start_step(execution_id, "filtering")
    Client->>DB: INSERT INTO execution_steps (status=RUNNING)
    Auto->>Auto: filter_relevant()
    Auto->>Client: finish_step(step_id)
    Client->>DB: UPDATE execution_steps SET status=SUCCESS

    Auto->>Client: finish_execution(execution_id)
    Client->>DB: UPDATE executions SET status=SUCCESS

    Note over FE,DB: Em paralelo, o usuário olha o dashboard

    FE->>API: GET /automations/english-news/executions/121
    API->>DB: SELECT execution + steps (via repository)
    DB-->>API: dados da execução
    API-->>FE: JSON com status de cada step
    FE->>FE: renderiza os steps (polling a cada 2s)

```

# fluxo

```
Fluxo:
  iniciar execução
      ↓
Método:
  start_execution()

Fluxo:
  iniciar fase
      ↓
Método:
  start_step()

Fluxo:
  terminar fase
      ↓
Método:
  finish_step()

Fluxo:
  registrar métricas
      ↓
Método:
  record_metric()
```
