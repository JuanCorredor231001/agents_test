from langchain_core.language_models.fake_chat_models import GenericFakeChatModel
from langchain_core.messages import AIMessage

from hermes_agent.agent import build_agent


class FakeToolModel(GenericFakeChatModel):
    def bind_tools(self, tools, **kwargs):
        return self


def test_agent_calls_tool_then_answers():
    msgs = iter([
        AIMessage(content="", tool_calls=[{"name": "calculator", "args": {"expression": "2+2"}, "id": "1"}]),
        AIMessage(content="El resultado es 4"),
    ])
    agent = build_agent(llm=FakeToolModel(messages=msgs))
    out = agent.invoke({"messages": [("user", "2+2?")]}, {"configurable": {"thread_id": "t"}})
    assert out["messages"][-1].content == "El resultado es 4"
    assert any(m.type == "tool" and m.content == "4" for m in out["messages"])
