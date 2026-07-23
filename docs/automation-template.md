# <Nome da Automação>

## Descrição

Objetivo principal e por quê ela existe.

## Dados de entrada

O que ela consome (API, arquivo, banco).

## Gatilho

- [ ] GitHub Actions
- [ ] systemd timer

## Fluxo

```mermaid
flowchart TD
    A[Início] --> B[...]
```

## Estrutura interna

- imports/dependências principais
- tabelas do banco usadas
- tempo de execução esperado

## Observabilidade

- onde ficam os logs
- tempo medido via `shared.observability`

## Trade-offs

(alimentar conforme for desenvolvendo)

## Componentes globais usados

Quais módulos de `shared` essa automação depende.

# temaplete install.sh

```
#!/bin/bash
echo "criando arquitetura"
uv init --package packages/nome-da-pasta
cd packages/nome-da-pasta
uv add dependencias-da-automacao
uv sync --all-packages
echo "
template init
" > __init__.py ou main.py
cd ../..
```
