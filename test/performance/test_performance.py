import psutil
import pytest
import time 
from shared.clients.client_orquestrator import OrchestratorClient
from english_news.manifest import manifest
from english_news.__init__ import main
print(manifest.slug)
import os 
@pytest.fixture
def client():
    return OrchestratorClient()

def run_automation():
    client = OrchestratorClient()

    execution_id = client.start_execution(manifest.slug)

    step_id = client.start_step(
        execution_id,
        "scraping"
    )

    client.finish_step(step_id)

    step_id = client.start_step(
        execution_id,
        "filtering"
    )

    client.finish_step(step_id)

    client.finish_execution(execution_id)
@pytest.mark.skip(reason="dont need now this automation did test of all real flow")
@pytest.mark.performance
def test_automation_englsih_news():
    process = psutil.Process(os.getpid())
    init = time.perf_counter()
    main()
    end = time.perf_counter()
    elapsed_time = end - init
    print()
    print("\n ======[red]estatisticas[/red]========")
    print(f"Tempo de execução: {elapsed_time:.2f} segundos")
    print(f"CPU: {process.cpu_percent(interval=0.1)}%")
    print(f"Memória: {process.memory_info().rss / 1024**2:.2f} MB")
    print(f"Threads: {process.num_threads()}")
@pytest.mark.skip(reason="nao precisa rodar o teste sempre")
@pytest.mark.performance
def test_start_execution_benchmark_english_news_db(benchmark):
     """aqui é o teste benchmark real do neon"""
     benchmark(
    run_automation
    )
@pytest.mark.performance
def test_automation_english_news(db_handler,automation_seed):
    process = psutil.Process(os.getpid())
    client = OrchestratorClient(
        connection_string=db_handler.database_url
    )
    init = time.perf_counter()
    execution_id = client.start_execution(manifest.slug)
    step_id = client.start_step(execution_id, "scraping")
    print("Scraping...")
    client.finish_step(step_id)
    step_id = client.start_step(execution_id, "filtering")

    print("filtering...")
    client.finish_step(step_id)
    client.finish_execution(execution_id)
    end = time.perf_counter()
    elapsed_time = end - init
    print()
    print("\n ======[red]estatisticas[/red]========")
    print(f"Tempo de execução: {elapsed_time:.2f} segundos")
    print(f"CPU: {process.cpu_percent(interval=0.1)}%")
    print(f"Memória: {process.memory_info().rss / 1024**2:.2f} MB")
    print(f"Threads: {process.num_threads()}")