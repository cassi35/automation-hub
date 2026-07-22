# objetivo

nesse repositorio o objetivo é criar um projeto com automocoes independentes rodando ao iniciar linux
github actions e database local , para organizacao das tarefas locais , automacoes de codigo .
o sistema se comporta como se fosse a orgaizacao,
focamdno em automcocoes com performance , codigos limpos
e bem documentados

# idea geral

Cada automação declara os próprios metadados no código (nome, descrição, tipo de gatilho) — isso é estático, não muda a cada execução.
Um comando de sync lê essas declarações de todos os pacotes e sincroniza (upsert) com o banco.
Quando a automação executa de fato (uv run python.py), ela só grava o histórico de execução (começou, terminou, sucesso/falha) — não recadastra ela mesma.

# rules

- **init**.py para facilitacao dos imports
- replace strtucutre with automation
- tests in every automation

# global share

- env
- logger
- db
- thread
- rabbitmq

# ARCHTECRE

- ./github
- uv.lock
- congig
- env.py
- shared
- packges
- aqui seram as automocoes

# shared

pasta shared aqui que vira a ponte global para automacoes

## exemplo

- new-scrapper
  README.MD
- no readme tem que conter:

1.  name
2.  description --> contendo objetivo da automacao detalhado e o porque
    > tem que responder as perguntas

- CRIAR COM CLAUDE

3.  strtcuture
    > nesse strtucuture é uma lista sobre quais sao

- imports
- dependencias
- db
- tempo de execucao esperado
- (guthub actions /systeammd) gatilho
- fluxo da automacao --> mermeid ou markdown mesmo

4. trade off
   > nessa parte vou detalhar os prazos para a criacao

- systeamd
  nessa pasta vao ser os .service para rodar as automacoes locais vou usar

# security

- scripts de redes para testar seguranca
- somente dados mocados

# packdge

cada packgde é uma automacao individual e nela vou aplicar o readme expicativo
detalhado sobre o porque qual beneficio

# automation

### objetyivo

- identificacao de padroes e criacao de skills para codex
- configuracao de jira e metricas
- server mcp global para criacao chamar db etc

# folders

systeamd /
rodar units local
new.service

# scripts

symlink dos .service pro systemd --user
/scripts
install-service.sh

# .env

aqui vao ser as env que vou chamar com a criacao das automacoes

# requirements

1. ## funcional
2. ## non funcional

# restrictions

- nao usar lib pesadas

# te,plates

- ## .github/workflows/ci.yml

```name: CI
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
      - run: uv sync --all-packages
      - run: uv run pytest

```

- ## systemd/news-scraper.timer:

```[Unit]
Description=Roda o news-scraper todo dia às 8h

[Timer]
OnCalendar=*-*-* 08:00:00
Persistent=true

[Install]
Wa`tedBy=timers.target
```

# Diretrizes de Contribuição & Workflow

## 1. adicionar backlog

nessa fase eu vou observar o readme criado e ir adicinando de acordo com o reamde

1. nome
2. descricao

- objetivo principal
- tempo
- skills ide utilizado

3. subtarefas do que sera feito
4. configuracoes do desenvolvimento

- branch
- commit

5. automacao para o jira se fizer sentido

# automation strtucture folder

- README.md
- main.py
- strtcutre

# automation readme.md

> aqui é a parte aonde vou falar da estrtura principal padrao para todas as automocoes

- titulo
- descricao objetivo principal
- dados de entrada
- utilizacao github actions , ou syseamd
- mermeid fluxo
- logs e observialidade
- utilizacao de componentes globais
- configuracoes jira
- install.sh nos scripts para automacao do template

# packges / shared

orchestrator/services/ → lógica do control plane (pause/resume/list automations). Só o orchestrator usa.
packages/shared/ → lógica de negócio compartilhada entre automações (ex: ExecutionTracker, um NotionClient, um TextSummarizer). Cada automação faz uv add shared --package news-scraper pra importar.

# .env

aqui seram meus enviroments que vou usar para o projeto

- JIRA_TKOEN
- MICROSOFT_GRAPH

# init project

1. chmod +x scrpts/init/install.sh
2. scrpts/init/install.sh
