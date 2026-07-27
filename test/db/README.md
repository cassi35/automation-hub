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
