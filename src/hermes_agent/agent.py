from langchain.agents import create_agent
from langchain_core.language_models import BaseChatModel
from langgraph.checkpoint.memory import InMemorySaver

from .llm import build_llm
from .tools import TOOLS

SYSTEM_PROMPT = (
    "Eres un agente útil basado en Hermes. Usa las herramientas cuando "
    "ayuden a responder con precisión; si no las necesitas, responde directo. "
    "Responde en el idioma del usuario."
)


def build_agent(llm: BaseChatModel | None = None, tools=None):
    return create_agent(
        model=llm or build_llm(),
        tools=tools or TOOLS,
        system_prompt=SYSTEM_PROMPT,
        checkpointer=InMemorySaver(),  # memoria por thread_id
    )
