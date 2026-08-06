from rich import print
import pytest
@pytest.mark.unit
def test_get_by_id(repo_execution,automation_model,db_session,execution_model):
       db_session.add(automation_model)
       db_session.commit()
       result = repo_execution.get_by_execution_id(execution_model.id)
       print(result)
       assert result.id == execution_model.id
@pytest.mark.unit
def test_list_by_automation_id(repo_execution,automation_model,db_session,execution_model):
    db_session.add(automation_model)
    db_session.commit()

    executions = repo_execution.list_by_automation_id(
        automation_model.id
    )

    assert len(executions) == 1
    assert executions[0].automation_id == automation_model.id
@pytest.mark.unit
def test_list_by_automation_id_not_found(
    repo_execution,
):
    result = repo_execution.list_by_automation_id(999999)

    assert result is None


@pytest.mark.unit
def test_list_by_automation_id_without_executions(
    repo_execution,
    db_session,
     automation_model,
):

    db_session.add(automation_model)
    db_session.commit()

    result = repo_execution.list_by_automation_id(
        automation_model.id
    )

    assert result == []


@pytest.mark.unit
def test_get_steps(
    repo_execution,
    automation_model,
    execution_model,
    step_model,
    db_session,
):
    db_session.add(automation_model)
    db_session.commit()

    steps = repo_execution.get_steps(
        execution_model.id
    )

    assert len(steps) == 1
    assert steps[0].id == step_model.id
    assert steps[0].execution_id == execution_model.id
    assert steps[0].name == step_model.name
    assert steps[0].status == step_model.status


@pytest.mark.unit
def test_get_steps_without_steps(
    repo_execution,
    automation_model,
    db_session,
    execution_model
):


    db_session.add(automation_model)
    db_session.commit()

    steps = repo_execution.get_steps(execution_model.id)

    assert steps == []


@pytest.mark.unit
def test_get_by_automation_id(
    repo_execution,
    automation_model,
    execution_model,
    db_session,
):
    db_session.add(automation_model)
    db_session.commit()

    result = repo_execution.get_by_automation_id(
        automation_model.id
    )

    assert result is not None
    assert result.id == execution_model.id
    assert result.automation_id == automation_model.id


@pytest.mark.unit
def test_get_by_automation_id_without_execution(
    repo_execution,
    db_session,
    automation_model
):
  

    db_session.add(automation_model)
    db_session.commit()

    result = repo_execution.get_by_automation_id(
        automation_model.id
    )

    assert result is None


@pytest.mark.unit
def test_get_executions_by_slug(
    repo_execution,
    automation_model,
    execution_model,
    db_session,
):
    db_session.add(automation_model)
    db_session.commit()

    result = repo_execution.get_executions_by_slug(
        automation_model.slug
    )

    assert len(result) == 1
    assert result[0].id == execution_model.id
    assert result[0].automation_id == automation_model.id


@pytest.mark.unit
def test_get_executions_by_slug_not_found(
    repo_execution,
):
    result = repo_execution.get_executions_by_slug(
        "slug-inexistente"
    )

    assert result == []


@pytest.mark.unit
def test_get_executions_by_slug_without_execution(
    repo_execution,
    db_session,
    automation_model
):

    db_session.add(automation_model)
    db_session.commit()

    result = repo_execution.get_executions_by_slug(
        automation_model.slug
    )

    assert result == []