from shared.clients.client_orquestrator import OrchestratorClient
from rich import print
import time
import requests
from monitor_juridico.manifest import manifest
from monitor_juridico.email.email_service import send_email

def main() -> None:
    client = OrchestratorClient()
    execution_id = client.start_execution(manifest.slug)

    print("[bold green]start_execution[/bold green]")

    try:
        init = time.perf_counter()

        # Fase 1 - Consulta API do CNJ
        step_id = client.start_step(execution_id, "consulta_api_cnj")
        print("[cyan]Consulta API do CNJ...[/cyan]")
        print("  Consultar comunicações por OAB ou número de processo")
        print("  Consultar janela de datas")
        time.sleep(5)
        client.finish_step(step_id)

        # Fase 2 - Identificação de novas comunicações
        step_id = client.start_step(
            execution_id,
            "identificar_comunicacoes",
        )
        print("[yellow]Identificação de novas comunicações...[/yellow]")
        print("  Processar comunicações retornadas")
        print("  Comparar com registros existentes")
        print("  Identificar novas ocorrências")
        time.sleep(5)
        client.finish_step(step_id)

        # Fase 3 - Persistência
        step_id = client.start_step(execution_id, "persistencia")
        print("[magenta]Persistência...[/magenta]")
        print("  Registrar novas comunicações")
        print("  Evitar registros duplicados")
        time.sleep(5)
        client.finish_step(step_id)

        # Fase 4 - Emissão do evento
        step_id = client.start_step(execution_id, "emissao_evento")
        print("[blue]Emissão do evento...[/blue]")
        print("  Emitir evento para o Automation Hub")
        print("  Disponibilizar nova comunicação para o dashboard")
        time.sleep(5)
        client.finish_step(step_id)

        client.finish_execution(execution_id)
        send_email()
        elapsed_time = time.perf_counter() - init

        print("[bold green]finish_execution[/bold green]")
        print(f"Tempo de execução: {elapsed_time:.2f} segundos")

    except Exception as e:
        client.fail_execution(execution_id, str(e))
        raise


if __name__ == "__main__":
    main()