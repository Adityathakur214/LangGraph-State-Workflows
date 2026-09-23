from langgraph.graph import StateGraph,START,END
from typing import TypedDict

class State(TypedDict):
    a:int
    b:int
    sum:int
    mul:int

def add_node(state:State):
    return {"sum": state["a"] + state["b"]}

def mul_node(state:State):
    return {"mul": state["sum"] * state["a"]}

builder = StateGraph(State)
builder.add_node("add_node", add_node)
builder.add_node("mul_node", mul_node)
builder.add_edge(START, "add_node")
builder.add_edge("add_node", "mul_node")    
builder.add_edge("mul_node", END)

graph = builder.compile()
result = graph.invoke({"a": 10, "b": 20})
print(result)