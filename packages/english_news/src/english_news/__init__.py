from shared.clients.client_orquestrator import OrchestratorClient
from rich import print
import time
import psutil
import os
from english_news.manifest import manifest
from time import perf_counter
def main() -> None:
    client =  OrchestratorClient()
    process = psutil.Process(os.getpid())
    execution_id = client.start_execution(manifest.slug)
    print(f"start_execution")
    try:
            init = time.perf_counter()
            step_id = client.start_step(execution_id, "scraping")
            print("Scraping...")
            client.finish_step(step_id)
            step_id = client.start_step(execution_id, "filtering")

            print("filtering...")
            client.finish_step(step_id)
            client.finish_execution(execution_id)
            end = time.perf_counter()
            elapsed_time = end - init
            print(f"Tempo de execução: {elapsed_time:.2f} segundos")
    except Exception as e:
        client.fail_execution(execution_id, str(e))
        raise

if __name__ == "__main__":
    main()

ideias = [
    "criar cores diferentes para cada step"
]