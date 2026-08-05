---
name: makerstructure
description: skill para criacao de estrtura e testes
---

# Purpose

objetivo é a criacao de testes unitarios, de integracao, performance e e2e para os modulos do projeto.

# workflow

1. entenda o que deve ser testado (respotory , service , etc)
2. defina qual tipo de teste deve ser criado (unit , integration , performance)

- **como** ?
  ...

3. leia brevemente o README.md na pasta test/
4. crie o arquivo dentro de uma delas em /test (integration,unit, performance,mcp) com touch test\_<nome_do_teste>.py
5. implmente os testes com as instrucoes abaixo
6. rode os testes comando: **uv run pytest -m test/<pasta>/<nome_do_aquivo_test>.py**
7. rode testes individualmente para garantir que tudo está funcionando depois coloque

```python
import pytest
@pytest.mark.skip() # isso nos testes que ja passaram
```

8. **opcional** se rodar commitar tudo o que fez individualmente chamando a skill
   **commit**

# estrtura testes

> aqui vai ser uma estrtura universal para todos os testes

1. **estrtura**

   ```python
   # imports corretos de acordo com o projeto
   import pytest
   # implementacoes de testes de performance
   # cada teste com @mark.performance
   @pytest.mark.performance # ou integration ou unit ou e2e
   def test_performance():
       # implementacao do teste de performance
       assert True # aqui são realizados os testes de verdade
   ```

# **REGRAS IMPORTANTES**

- rode primeiros testes individuais para garantir que tudo está funcionando e depois de um
- observe se os testes precisam de mock ou spy, se sim, crie um mock separado e use ele no teste

# referencies

- **folders**
- modules.yaml
- test/README.md
