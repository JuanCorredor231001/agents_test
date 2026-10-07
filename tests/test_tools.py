from hermes_agent.tools import calculator, current_time


def test_calculator():
    assert calculator.invoke({"expression": "(2+3)*4/5"}) == "4.0"


def test_calculator_rejects_code():
    assert calculator.invoke({"expression": "__import__('os')"}).startswith("Error")


def test_time():
    assert "T" in current_time.invoke({})
