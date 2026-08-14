import time

from shared.config.config import Config

from automation_agent.utils.llm import LLMType, load_llm
def test_llm(llm_type: LLMType, prompt: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"MODEL: {llm_type.value}")
    print(f"{'=' * 60}")

    llm = load_llm(
        temperature=0,
        llm_type=llm_type,
    )   

    start = time.perf_counter()

    response = llm.invoke(prompt)

    elapsed = time.perf_counter() - start

    print(f"\nResponse:\n{response.content}")
    print(f"\nTime: {elapsed:.3f}s")


def main() -> None:
    prompt = "oi qual seu nome"
    test_llm(LLMType.GROQ, prompt)
    test_llm(LLMType.GOOGLE, prompt)
if __name__ == "__main__":
    main()