from contextlib import asynccontextmanager
from enum import Enum
from typing import AsyncGenerator

from langchain_core.language_models import BaseChatModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from shared.config.config import Config
class LLMType(str, Enum):
    OLLAMA = "ollama"
    GROQ = "groq"
    GOOGLE = "google"


def load_llm(
    temperature: float,
    llm_type: LLMType,
) -> BaseChatModel:

    if llm_type == LLMType.OLLAMA:
        return ChatOllama(
            model=Config.LLM_MODEL,
            temperature=temperature,
        )

    if llm_type == LLMType.GROQ:
        return ChatOpenAI(
            model=Config.LLM_MODEL_GROQ,
            temperature=temperature,
            api_key=SecretStr(Config.GROQ_API),
            base_url="https://api.groq.com/openai/v1",
        )

    if llm_type == LLMType.GOOGLE:
        return ChatGoogleGenerativeAI(
            model=Config.LLM_MODEL_GOOGLE,
            temperature=temperature,
            google_api_key=Config.GOOGLE_STDIO_API,
        )

    raise ValueError(f"Unsupported LLM type: {llm_type}")
@asynccontextmanager
async def async_lifespan() -> AsyncGenerator[None, None]:
    print("async abri")
    yield
    print("async fechei")