from langgraph.graph import StateGraph, START, END
from typing import TypedDict


class State(TypedDict):
    query: str
    result: str
    iterations: int
    complete: bool


def process_node(state: State):
    iteration = state["iterations"] + 1
    result = f"Processed '{state['query']}' (iteration {iteration})"
    

    return {
        "result": result,
        "iterations": iteration,
        "complete": iteration >= 3,
    }


def should_continue(state: State):
    if state["complete"]:
        return "end"

    return "loop"


builder = StateGraph(State)
builder.add_node("Process", process_node)
builder.add_edge(START, "Process")
builder.add_conditional_edges(
    "Process",
    should_continue,
    {
        "loop": "Process",
        "end": END,
    },
)

graph = builder.compile()

result = graph.invoke(
    {
        "query": "build a LangGraph loop",
        "result": "",
        "iterations": 0,
        "complete": False,
    }
)

print(result)