# Agente con HuggingFace + LangChain + Hermes

- **Hermes** (NousResearch) – LLM con soporte nativo de tool-calling (`<tool_call>`).
- **HuggingFace** – hospeda el modelo (Inference Providers) y `langchain-huggingface`.
- **LangChain** – orquestación del agente (`create_agent`, tools, memoria).

## Proceso paso a paso

1. **Entorno**
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt && pip install -e .
   cp .env.example .env     # añade tu HUGGINGFACEHUB_API_TOKEN
   ```
2. **Elegir backend** (`LLM_BACKEND` en `.env`)
   - `hf`: API de HuggingFace (más simple, requiere token y que el modelo esté disponible en un provider).
   - `local`: servidor OpenAI-compatible con GPU, p. ej.
     `vllm serve NousResearch/Hermes-3-Llama-3.1-8B --enable-auto-tool-choice --tool-call-parser hermes`
     (o Ollama: `ollama run hermes3`, con `LOCAL_BASE_URL=http://localhost:11434/v1`).
3. **Probar**: `pytest` (usa un modelo falso, sin red) y `python -m hermes_agent.cli`.
4. **Añadir herramientas** en `src/hermes_agent/tools.py` (decorador `@tool` + lista `TOOLS`).
5. **Evolucionar**: RAG, memoria persistente, API (FastAPI), evaluación, observabilidad (LangSmith).

## Estructura
```
src/hermes_agent/  config.py · llm.py · tools.py · agent.py · cli.py
tests/             tools y bucle del agente con modelo falso
```

## Opciones de proyecto

| # | Proyecto | Tools / piezas | Dificultad |
|---|----------|----------------|-----------|
| 1 | **Asistente RAG sobre tus documentos** (PDF/Markdown) | `langchain-huggingface` embeddings (`BAAI/bge-small`), FAISS/Chroma, tool `search_docs` | Baja |
| 2 | **Analista de datos (CSV/SQL)** | tool SQL (SQLite), tool Python sandbox, gráficos | Media |
| 3 | **Agente de investigación web** | búsqueda (Tavily/DuckDuckGo), lectura de URLs, informe con citas | Media |
| 4 | **Asistente de código / revisor de PRs** | tools GitHub (leer diff, comentar), linters | Media |
| 5 | **Bot de soporte multi-herramienta** (Telegram/Slack) | FastAPI + memoria persistente (SQLite checkpointer), tools de tickets/FAQ | Media |
| 6 | **Sistema multi-agente** (planificador + ejecutores) | LangGraph supervisor, Hermes como planner y un modelo pequeño como worker | Alta |
| 7 | **Agente con fine-tuning** | dataset de tool-calls en HF Hub, LoRA sobre Hermes, evaluación | Alta |

Recomendado para empezar: **#1 (RAG)** — es el que más valor da con menos código; luego #5 para exponerlo como servicio.
