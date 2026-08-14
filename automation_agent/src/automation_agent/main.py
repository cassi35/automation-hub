from langchain_ollama import ChatOllama
import time


def main() -> None:
    llm = ChatOllama(
        model="phi4-mini:latest ",
        temperature=0,
    )

    start = time.perf_counter()

    response = llm.invoke(
        "quanto é 2 * 2 "
    )

    elapsed = time.perf_counter() - start

    print(response.content)
    print(f"Tempo de execução: {elapsed:.3f}s")