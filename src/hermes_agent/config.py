import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    backend: str = os.getenv("LLM_BACKEND", "hf")
    model: str = os.getenv("HERMES_MODEL", "NousResearch/Hermes-3-Llama-3.1-8B")
    local_base_url: str = os.getenv("LOCAL_BASE_URL", "http://localhost:8000/v1")
    local_api_key: str = os.getenv("LOCAL_API_KEY", "not-needed")
    temperature: float = float(os.getenv("TEMPERATURE", "0.2"))
    max_tokens: int = int(os.getenv("MAX_TOKENS", "1024"))


settings = Settings()
