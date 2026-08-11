---
name: testfixture
description: skill de cricao de fixture
---

# objetivo

identificacao de mocks e fuxtures que se repetem em mais de um arquivo de teste ou se for pedido para criar uma fixture para importar em um teste especifico.

# fluxo

1. identificar duplicidade em arquivos dado de contexto ou identificar o que foi pedido para criar uma fixture
2. na pasta test/fixtures crie um arquivo com touch fixture\_<nome_da_fixture>.py
3. faca a implmentacao da fixture dentro do arquivo criado com a estrtura

- **exemplo**

```python
import pytest
from shared.db.entities.automation import AutomationModel,ExecutionModel,MetricModel,StepModel
@pytest.fixture()
def step_model_fixture():
    return StepModel(
        id=1,
        name="Test Step",
        description="This is a test step",
        execution_id=1,
        status="pending"
    )
  ... # assim sucessivamente
```

4. chame as fixtures nos testes que precisam ser chamados nos arquivos
5. **opcional** se for pedido para testar teste com **uv run pytest <caminho_do_arquivo>.py**
