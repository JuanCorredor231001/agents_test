import sys

from .agent import build_agent


def main() -> None:
    agent = build_agent()
    cfg = {"configurable": {"thread_id": "cli"}}
    print("Agente Hermes listo. Ctrl+C para salir.")
    while True:
        try:
            q = input("tú> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit(0)
        if not q:
            continue
        out = agent.invoke({"messages": [("user", q)]}, cfg)
        print("agente>", out["messages"][-1].content)


if __name__ == "__main__":
    main()
