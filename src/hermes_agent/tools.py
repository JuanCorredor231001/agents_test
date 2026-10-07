import ast
import operator
from datetime import datetime, timezone

from langchain_core.tools import tool

_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def _eval(node: ast.AST) -> float:
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval(node.operand))
    raise ValueError("Expresión no permitida")


@tool
def calculator(expression: str) -> str:
    """Evalúa una expresión aritmética segura, ej. '(2+3)*4/5'."""
    try:
        return str(_eval(ast.parse(expression, mode="eval").body))
    except Exception as e:
        return f"Error: {e}"


@tool
def current_time() -> str:
    """Devuelve la fecha y hora actual en UTC (ISO 8601)."""
    return datetime.now(timezone.utc).isoformat()


# Añade aquí tus herramientas (búsqueda web, RAG, SQL, APIs...).
TOOLS = [calculator, current_time]
