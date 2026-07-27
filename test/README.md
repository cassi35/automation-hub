# objetivo

nessa camada se testa diferentes niveis da db ,

# testes

## db 1

1. unitarios

- apenes contrucao do objeto em python

## db 2

1. Integration test: banco real
   Python
   ↓
   SQLAlchemy
   ↓
   PostgreSQL
   ↓
   Neon
2. teste de realacionamento

- Então você pode criar uma árvore real:

3. Testar cascade delete

- Esse é exatamente o tipo de coisa que não faz sentido testar apenas com mock.

5. Testar constraints

- **EX**

```
name = Column(
    String(30),
    nullable=False,
)
automation = AutomationModel(
    name=None,
    trigger="system",
    status="active",
)

db_session.add(automation)

with pytest.raises(IntegrityError):
    db_session.commit()

```

# fluxo

```

uv run pytest

      ↓

conftest.py

      ↓

TestDatabaseHandler

      ↓

Testcontainer sobe

      ↓

URL temporária

      ↓

DATABASE_URL sobrescrita

      ↓

cd apps/automations-hub

uv run alembic upgrade head

      ↓

migrations aplicadas no PostgreSQL temporário

      ↓

testes usam o banco

      ↓

pytest termina

      ↓

container destruído

```

# meu config.py

```

```

Esse teste se enquadra na categoria de **`@pytest.mark.integration`** (Teste de Integração).

### Por que ele é de Integração e não Unitário?

1. **Dependência de Recurso Externo (`db_session`):** Ele faz comunicação real com o banco de dados via SQLAlchemy (`add`, `commit`, `get`). Testes unitários puros rodam estritamente em memória/isolados sem acesso a IO, drivers de rede ou banco.
2. **Validação da Camada de Persistência (ORM):** Ele valida se o mapeamento relacionais em cascata (`Automation` -> `Execution` -> `Step` -> `Metric`) e as chaves estrangeiras funcionam corretamente no banco de dados real.

---

### Exemplo de Aplicação

Você deve decorá-lo assim:

```python
import pytest

@pytest.mark.integration
def test_cria_arvore_completa(db_session):
    """aqui testa o relacionamento completo entre as entidades"""
    # ... código do teste

```

### Categorização Geral de Marcadores para a Suíte

| Tipo de Teste     | Marcador Recomendado       | O que testa                                                                      | Exemplo                                                                                                   |
| ----------------- | -------------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Unitário**      | `@pytest.mark.unit`        | Regras de negócio puras, métodos utilitários, validações Pydantic                | Testar se uma função de calcular desconto retorna o valor correto.                                        |
| **Integração**    | `@pytest.mark.integration` | Comunicação entre módulos, repositórios com BD, rotas da API com banco de testes | Testar se o SQLAlchemy grava e recupera entidades em cascata (seu teste atual).                           |
| **Ponta a Ponta** | `@pytest.mark.e2e`         | Fluxo completo do sistema cruzando várias camadas/serviços externos              | Chamar um endpoint HTTP que dispara uma automação, grava no banco e envia uma mensagem para fila/webhook. |
