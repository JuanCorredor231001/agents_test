from langchain_core.language_models import BaseChatModel

from .config import Settings, settings as default_settings


def build_llm(cfg: Settings = default_settings) -> BaseChatModel:
    """Construye el chat model de Hermes según el backend configurado."""
    if cfg.backend == "hf":
        from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

        endpoint = HuggingFaceEndpoint(
            repo_id=cfg.model,
            task="text-generation",
            max_new_tokens=cfg.max_tokens,
            temperature=cfg.temperature,
        )
        return ChatHuggingFace(llm=endpoint)

    if cfg.backend == "local":
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(
            model=cfg.model,
            base_url=cfg.local_base_url,
            api_key=cfg.local_api_key,
            temperature=cfg.temperature,
            max_tokens=cfg.max_tokens,
        )

    raise ValueError(f"LLM_BACKEND desconocido: {cfg.backend!r} (usa 'hf' o 'local')")
