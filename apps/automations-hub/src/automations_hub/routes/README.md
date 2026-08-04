# objetivo

esse readme que é a skill vai ser usado para automacao da criacao de services e rotas

# objetivo service

no serve é aonde vao ser os metodos chamados nas rotas, os arquivos de rotas sao classes

# exemplo

```
# importacoes
from automations_hub.infra.automation_repository import AutomationRepository
from automations_hub.errors.exceptions import InvalidAutomationSlug ... etc
# classe principal
class AutomationService:
def __init__(self):
__repo = AutomationRepository()

```

# implementacoes dos metodos

async def automation_by_id(id:int)-> list[AutomationDto]
async def get_automation_by_id(int)-> AutomationDto
async def pause_automation(id:int)-> None
async def get_executions_by_automation_id(automation_id)-> list[ExecutionDto]

# metodos execution e automation

```
async def automation_get_all()-> automationDto
async def
# regras

- cada validacao verifique se precisa importar mais errors

# objetivo route

aqui vao ser todas as rotas de automation-hub que tem como objetivo
fazer estilo crud api

```

GET /automations → lista todas as automações
GET /automations/{slug} → detalhe de uma automação
PATCH /automations/{slug}/pause → pausa
PATCH /automations/{slug}/resume → retoma
POST /automations/{slug}/trigger → dispara execução manual

GET /automations/{slug}/executions → histórico de execuções dessa automação
GET /executions/{execution_id} → detalhe de uma execução (com steps)
GET /executions/{execution_id}/steps → só os steps dessa execução

GET /automations/{slug}/stats → taxa de sucesso, duração média (opcional, vem depois)

```

# explicacao

nao precisa de middlware porque vai rodar localmente

# passos

1. ## estrtura

```

# imports nescessarios

from fastapi.responses import JSONResponse
from fastapi import APIRouter,Depends,status,BackgroundTasks

# criacao das constantes das rotas

# exemplo

- exection_router = APIRouter()
- exection_service = ExecutionService()

# rotas

@exection_router.get('/executions/{automation_id}')
async def get_all_execution_by_automation_id(automation_id:str):
return exection_service.get_all_execution_by_automation_id()
...
assim por diante

```

2. ## declarar
1. declaracao das rotas no main.py

## exemplo main.py

```

# importacoes

from automations_hub.routes.execution import exection_router

# final do arquivo

@app.include_router(exection_router,prefix=f"/api/{version}/executions",tags=["executions"])

```

2. ## teste e2e
1. criar na pasta e2e test/e2e um arquivo chamado da api
1. ## estrtura

```

from apps.automation-hub.main import app ## testear os imports corretos
import requests
import pytest

## contantes

## fazer as declaracoes

# exemplo

@pytest.mark.e2e
def test_get_all_executions_by_automation_id():
""" aqui tem que ser a descricao breve do teste"""
response = requests.get('rota completa com id ')
assert response.status_code == 200
assets que fazem sentido com a descricao da execucao

```

2. **rodar os testes**
1. uv run python test -s test/caminhodoteste
1. verificar o que erro
   **pode chamar o servidor mcp para verificar**

- refatore os testes que estao errados

3. **colocar no uv e github actions** **opcional**

- verificar se e2e ja tem nos marcadores se nao tiver colocar para e2e
  markers = [
  .. resto
  "e2e": testes de http
  ]
- teste com o comando uv run -s e2e
  se passou comitar
- **github actions**
  quero que nessa fase coloque no github actions
  se nao tiver ainda

## regras

- não quero que altere saia alterando tudo sem a minha permissao
- cada rota bem sucessidida quero que tu faca um commit
- pode chamar os servidores mcp para verificar algo
- quero que faca
- sempre colocar readme nas pastas do que cada fase faz
- se nao entender me perguntar que eu vou explicar
- sempre tiver rodando o servidor
```
