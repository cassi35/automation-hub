from shared.clients.client_orquestrator import OrchestratorClient
from rich import print

from packages.english_news.manifest import manifest
def main() -> None:
    client =  OrchestratorClient()
    execution_id = client.start_execution(manifest.name)
    try:
        step_id = client.start_step(execution_id,"scraping")
        print("Scraping...")
        print("concluido step")
        client.finish_step(step_id)
        step_id = client.start_step(execution_id,"filtering")
        print("filtering...")
        print("concluido step")
        client.finish_step(step_id)
        client.finish_execution(execution_id)
    except Exception as e:
        client.fail_execution(execution_id, str(e))
        raise

if __name__ == "__main__":
    main()

ideias = [
    "criar cores diferentes para cada step"
]