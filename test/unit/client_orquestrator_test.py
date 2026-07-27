import pytest
from shared.db.entities.automation import AutomationModel,ExecutionModel,StepModel
from shared.clients.client_orquestrator import OrchestratorClient


@pytest.mark.integration
def test_start_execution_cria_execution_com_status_process(db_session, db_handler):
    automation = AutomationModel(name="job-orq", trigger="system", status="active")
    db_session.add(automation)
    db_session.commit()

    client = OrchestratorClient(connection_string=db_handler.database_url)
    execution_id = client.start_execution("job-orq")

    saved = db_session.get(ExecutionModel, execution_id)
    assert saved is not None
    assert saved.status == "process"


@pytest.mark.integration
def test_start_execution_automation_inexistente_falha(db_handler):
    client = OrchestratorClient(connection_string=db_handler.database_url)
    with pytest.raises(Exception, match="Automation not found"):
        client.start_execution("nao-existe")


@pytest.mark.integration
def test_fluxo_completo_finish_execution(db_session, db_handler):
    automation = AutomationModel(name="job-fluxo", trigger="system", status="active")
    db_session.add(automation)
    db_session.commit()

    client = OrchestratorClient(connection_string=db_handler.database_url)
    execution_id = client.start_execution("job-fluxo")
    step_id = client.start_step(execution_id, "build")
    client.finish_step(step_id)
    client.finish_execution(execution_id)

    step = db_session.get(StepModel, step_id)
    execution = db_session.get(ExecutionModel, execution_id)
    assert step.status == "stopped"
    assert execution.status == "success"
    assert execution.end_at is not None