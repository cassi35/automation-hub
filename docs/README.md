# objetivo

nesse repositorio o objetivo é criar um projeto com automocoes independentes rodando ao iniciar linux
github actions e database local , para organizacao das tarefas locais , automacoes de codigo .
o sistema se comporta como se fosse a orgaizacao,
focamdno em automcocoes com performance , codigos limpos
e bem documentados

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

- identificacao de padroes e criacao de skills para codex
- configuracao de jira e metricas
- server mcp global para criacao chamar db etc

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

## 1.

# automation strtucture

- README.md
- main.py

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
