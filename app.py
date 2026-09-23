from langgraph.graph import StateGraph, START, END
from typing import TypedDict


class State(TypedDict):
    name: str
    greetings: str


def name_node(state: State):
    return {"name": state["name"]}


def greetings_node(state: State):
    return {"greetings": "Hello " + state["name"] + "!"}


builder = StateGraph(State)
builder.add_node("name_node", name_node)
builder.add_node("greetings_node", greetings_node)
builder.add_edge(START, "name_node")
builder.add_edge("name_node", "greetings_node")
builder.add_edge("greetings_node", END)

graph = builder.compile()
result = graph.invoke({"name": "Gourav"})
print(result)