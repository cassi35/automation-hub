# Orchestrator API

## Objetivo

O `orchestrator-api` é o **control plane** do `organize-tasks`: o serviço que sabe
quais automações existem, qual o status de cada uma, o histórico de execuções,
e consegue pausar/reativar cada uma — sem precisar entrar em cada automação
individualmente pra saber o que está acontecendo.

Ele **não executa** as automações. As automações (`packages/*`) rodam sozinhas,
disparadas por systemd timers ou GitHub Actions, e escrevem seu próprio
histórico de execução direto no banco (via `ExecutionTracker`, em `packages/shared`).
O orchestrator só **lê** esses dados e expõe uma API + dashboard pra visualizar
e controlar o conjunto.

Isso separa duas responsabilidades que, se misturadas, viram bagunça:

- **Controle** (orchestrator): status, histórico, pause/resume, visão geral
- **Execução** (packages/\*): o trabalho de fato de cada automação

## O que ele resolve

Sem isso, cada automação é uma ilha — pra saber se rodou, se falhou, se está
ativa, você teria que entrar em cada uma, olhar log por log, lembrar
manualmente o que está pausado. O orchestrator centraliza isso:

- **Automations**: cadastro de cada automação (nome, descrição, tipo de
  gatilho, status atual)
- **Executions**: histórico de cada rodada (quando começou/terminou,
  sucesso/falha, duração, log)
- **Pause/Resume**: desabilita ou reabilita o gatilho de uma automação
  (`systemctl --user disable/enable <nome>.timer` por baixo dos panos)

## Arquitetura interna

| Camada      | Responsabilidade                                                                                         |
| ----------- | -------------------------------------------------------------------------------------------------------- |
| `api/`      | Rotas HTTP. Fino — só recebe request e chama o `services/`                                               |
| `domain/`   | Regras de negócio puras (ex: "automação pausada não inicia execução"). Zero import de FastAPI/SQLAlchemy |
| `services/` | Junta `domain/` + `infra/` pra executar uma operação completa (ex: `pause_automation`)                   |
| `infra/`    | Acesso a banco (SQLAlchemy/Postgres) e controle real dos processos (systemd)                             |

## Como automações se conectam a isso

As automações **não chamam essa API por HTTP**. Elas escrevem direto na
tabela `executions` do banco (via `packages/shared`), então o orchestrator
funciona só como leitor + painel de controle — ele não precisa estar de pé
pra uma automação rodar via systemd timer, só o banco precisa estar acessível.

# comandos docker

- docker build -t automations-hub .
- docker ps -a
- docker run -p 8000:8000 automations-hub
- docker start nomedocontainer

# comandos

- sudo lsof -i :8000 --> matar o processo
- sudo kill -9 <pid>
