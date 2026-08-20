from shared.clients.client_orquestrator import OrchestratorClient
from rich import print
import time
from english_news.manifest import manifest


def main() -> None:
    client = OrchestratorClient()
    execution_id = client.start_execution(manifest.slug)

    print("[bold green]start_execution[/bold green]")

    try:
        init = time.perf_counter()

        # Fase 1 - Scraping
        step_id = client.start_step(execution_id, "scraping")
        print("[cyan]Scraping...[/cyan]")
        time.sleep(5)
        client.finish_step(step_id)

        # Fase 2 - Processamento e filtragem
        step_id = client.start_step(execution_id, "processing")
        print("[yellow]Processamento e filtragem...[/yellow]")

        print("  Calcular quantidade de palavras")
        print("  Estimar tempo de leitura")
        print("  Classificar tópicos")
        print("  Descartar textos irrelevantes")
        print("  Ordenar por relevância")

        time.sleep(5)
        client.finish_step(step_id)

        # Fase 3 - Limite de tempo
        step_id = client.start_step(execution_id, "time_constraint")
        print("[magenta]Limite de tempo...[/magenta]")
        print("  Selecionar notícias até 45 minutos de leitura")

        time.sleep(5)
        client.finish_step(step_id)

        # Fase 4 - Geração de conteúdo
        step_id = client.start_step(execution_id, "content_generation")
        print("[blue]Geração de conteúdo...[/blue]")
        print("  Gerar prompts determinísticos")
        print("  Extrair vocabulário")
        print("  Gerar questionário em inglês")

        time.sleep(5)
        client.finish_step(step_id)

        # Fase 5 - Integração
        step_id = client.start_step(execution_id, "integration")
        print("[red]Integração...[/red]")
        print("  Enviar tarefas para MS To-Do")
        print("  Registrar execução no PostgreSQL")

        time.sleep(5)
        client.finish_step(step_id)

        client.finish_execution(execution_id)

        elapsed_time = time.perf_counter() - init

        print("[bold green]finish_execution[/bold green]")
        print(f"Tempo de execução: {elapsed_time:.2f} segundos")

    except Exception as e:
        client.fail_execution(execution_id, str(e))
        raise


if __name__ == "__main__":
    main()