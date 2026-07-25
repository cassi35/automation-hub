class OrchestratorClient:
    def start_execution(self, automation_name: str) -> int:
        ...  # cria linha em Execution, status=RUNNING, retorna execution_id

    def start_step(self, execution_id: int, name: str) -> int:
        ...  # cria linha em ExecutionStep, status=RUNNING

    def finish_step(self, step_id: int) -> None:
        ...  # status=SUCCESS

    def fail_step(self, step_id: int, error: str) -> None:
        ...  # status=FAILED

    def finish_execution(self, execution_id: int) -> None:
        ...

    def fail_execution(self, execution_id: int, error: str) -> None:pass