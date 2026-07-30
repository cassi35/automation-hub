from shared.db.entities.automation import AutomationModel,ExecutionModel,MetricModel,StepModel
import pytest
from sqlalchemy.exc import IntegrityError,DataError
from rich import print
# @pytest.mark.unit # marcador personalizado para fazer testes rapidos usado para -m
@pytest.mark.integration 
def test_cria_arvore_completa(db_session):
    """ aqui testa o relacionamento completo entre as entidades """
    automation = AutomationModel(
        name="deploy-prod",
        trigger="github_actions",
        status="active",
        slug="deploy-prod",
    )
    execution = ExecutionModel(status="process", automation=automation)
    step = StepModel(name="build", status="running", execution=execution)
    metric = MetricModel(name="duration", value=120, step=step)

    db_session.add(automation)
    db_session.commit()
    saved = db_session.get(AutomationModel, automation.id)
    automation_json = {
        "name": saved.name,
        "trigger": saved.trigger,
        "status": saved.status,
        "description": saved.description,
        "executions": [
            {
                "status": execution.status,
                "start_at": execution.start_at,
                "end_at": execution.end_at,
                "steps": [
                    {
                        "name": step.name,
                        "status": step.status,
                        "metrics": [
                            {
                                "name": metric.name,
                                "value": metric.value,
                            }
                            for metric in step.metrics
                        ],
                    }
                    for step in execution.steps
                ],
            }
            for execution in saved.executions
        ],
    }
    print(automation_json)
    print(f"[blue]nome da operacao:[/blue] [yellow]{saved.name}[/yellow]  [green]sucesso![/green]")
    print(f"[blue]status da operacao:[/blue] [yellow]{saved.status}[/yellow]  [green]sucesso![/green]")
    print(f"[blue]trigger da operacao:[/blue] [yellow]{saved.trigger}[/yellow]  [green]sucesso![/green]")
    assert saved.executions[0].steps[0].metrics[0].value == 120

@pytest.mark.integration
def test_cascade_delete_automation_apaga_executions(db_session):
    """ testa se ao apagar uma automation, também apaga suas executions """
    automation = AutomationModel(slug="job-x", name="job-x", trigger="system", status="active")
    execution = ExecutionModel(status="process", automation=automation)
    db_session.add(automation)
    db_session.commit()

    execution_id = execution.id
    db_session.delete(automation)
    db_session.commit()

    assert db_session.get(ExecutionModel, execution_id) is None

@pytest.mark.integration
def test_cascade_delete_execution_apaga_steps(db_session):
    """ testa se ao apagar uma execution, também apaga seus steps """
    automation = AutomationModel(slug="job-y", name="job-y", trigger="system", status="active")
    execution = ExecutionModel(status="process", automation=automation)
    step = StepModel(name="lint", status="running", execution=execution)
    db_session.add(automation)
    db_session.commit()

    step_id = step.id
    db_session.delete(execution)
    db_session.commit()

    assert db_session.get(StepModel, step_id) is None
@pytest.mark.integration
def test_automation_sem_name_falha(db_session):
    """ testa se ao apagar uma execution, também apaga seus steps """
    automation = AutomationModel(name=None, trigger="system", status="active")
    db_session.add(automation)
    with pytest.raises(IntegrityError):
        db_session.commit()
@pytest.mark.integration
def test_trigger_invalido_falha(db_session):
    """aqui verifica se o enum de trigger eh valido nao  validacao mas regra do python"""
    automation = AutomationModel(name="job-z", trigger="valor_invalido", status="active")
    db_session.add(automation)
    with pytest.raises(DataError):  # troca por LookupError/DataError depois de rodar e ver qual é
        db_session.commit()
@pytest.mark.integration
def test_execution_com_automation_id_inexistente_falha(db_session):
    """Foreign key inválida (execution apontando pra automation que não existe)"""
    execution = ExecutionModel(status="process", automation_id=99999)
    db_session.add(execution)
    with pytest.raises(IntegrityError):
        db_session.commit()
@pytest.mark.integration
def test_name_maior_que_30_chars_falha(db_session):
    """ aqui é ver se a string é muito longa """
    automation = AutomationModel(
        name="a" * 31,
        trigger="system",
        status="active",
    )
    db_session.add(automation)
    with pytest.raises(Exception):  # Postgres normalmente dá erro de truncamento
        db_session.commit()
@pytest.mark.unit #b teste demostracao
def test_sum()->None:
    a = 1
    b = 2
    print(f"a + b = {a + b}")
