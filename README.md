# 🦜 LangGraph Fundamentals & State Workflows

A beginner-friendly repository demonstrating the **fundamentals of LangGraph** using Python.

This project covers how to build **stateful workflows**, pass data between nodes, create sequential execution pipelines, and implement **conditional loops** using `TypedDict` and LangGraph's graph-based architecture.

---

## 📌 What is LangGraph?

**LangGraph** is a framework for building stateful, multi-step applications and workflows with Python.

Instead of writing a simple linear sequence of functions, LangGraph allows you to represent your application as a **graph**, where:

* **Nodes** represent individual tasks or functions.
* **Edges** define the execution flow.
* **State** stores and passes information between nodes.
* **Conditional edges** allow workflows to make decisions.
* **Loops** allow a graph to repeatedly execute nodes until a condition is satisfied.

### Basic Workflow

```text
             ┌──────────────┐
             │    START     │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │     Node     │
             │   Process    │
             │    State     │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │     Node     │
             │   Process    │
             │    State     │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │     END      │
             └──────────────┘
```

---

# 📂 Project Structure

```text
LangGraph-Fundamentals/
│
├── app.py
├── test.py
├── classify.py
├── requirements.txt
└── README.md
```

---

# 🚀 Implementations

## 1. String Manipulation Workflow — `app.py`

This example demonstrates a simple **sequential LangGraph workflow** that processes a user's name and generates a greeting message.

### Workflow

```text
START
  │
  ▼
name_node
  │
  ▼
greetings_node
  │
  ▼
 END
```

### State

The workflow uses a state object containing the user's name.

```python
{
    "name": "Gourav"
}
```

### Processing

The graph performs two operations:

1. `name_node` processes the provided name.
2. `greetings_node` generates a greeting message.

### Example

**Input:**

```python
{
    "name": "Gourav"
}
```

**Output:**

```text
Hello Gourav!
```

### Concepts Demonstrated

* `StateGraph`
* `TypedDict`
* Nodes
* Edges
* `START`
* `END`
* Sequential execution
* State passing

---

# 2. Mathematical Operations Graph — `test.py`

This example demonstrates how numerical data can be passed between multiple nodes.

The graph performs mathematical operations sequentially.

### Workflow

```text
START
  │
  ▼
add_node
  │
  ▼
mul_node
  │
  ▼
 END
```

### Input

```python
{
    "a": 10,
    "b": 20
}
```

### Node 1 — `add_node`

The first node calculates the sum:

```text
sum = a + b
```

For the example:

```text
sum = 10 + 20
sum = 30
```

The updated state becomes conceptually:

```python
{
    "a": 10,
    "b": 20,
    "sum": 30
}
```

### Node 2 — `mul_node`

The second node uses the calculated `sum` and multiplies it by `a`:

```text
result = sum × a
```

Therefore:

```text
result = 30 × 10
result = 300
```

### Concepts Demonstrated

* Passing state between nodes
* Updating state
* Sequential node execution
* Mathematical processing
* Using previous node output in the next node

---

# 3. Iterative Processing & Conditional Loops — `classify.py`

This example demonstrates one of the important features of LangGraph:

> **Conditional execution and loops**

Instead of executing the graph only once, the workflow can repeatedly execute a node until a specific condition is satisfied.

### State Variables

The workflow maintains:

| Variable     | Purpose                                  |
| ------------ | ---------------------------------------- |
| `query`      | Stores the input query                   |
| `result`     | Stores the processing result             |
| `iterations` | Tracks the number of executions          |
| `complete`   | Indicates whether processing is finished |

The state is represented using `TypedDict`.

### Workflow

```text
              ┌──────────────┐
              │    START     │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │   Process    │
              │    Query     │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │   Condition  │
              └──────┬───────┘
                     │
              ┌──────┴───────┐
              │              │
        iterations < 3   iterations >= 3
              │              │
              ▼              ▼
          Process         ┌───────┐
          Again           │  END  │
              │           └───────┘
              │
              └───────────────┐
                              │
                              ▼
                           Process
```

### Loop Condition

The workflow continues processing while:

```text
iterations < 3
```

Once:

```text
iterations >= 3
```

the graph terminates and marks the process as complete.

### Final State

The final state contains:

```python
{
    "query": "...",
    "result": "...",
    "iterations": 3,
    "complete": True
}
```

### Concepts Demonstrated

* Conditional edges
* Iterative workflows
* Loop execution
* State updates
* Boolean completion flags
* Controlling graph termination

---

# 🧠 Core LangGraph Concepts Covered

This repository focuses on the following fundamentals:

### 1. State

State is the information shared between different nodes.

```python
class State(TypedDict):
    name: str
```

---

### 2. Nodes

A node represents an individual processing step.

```python
def my_node(state):
    # process state
    return state
```

---

### 3. Edges

Edges define how execution moves from one node to another.

```text
Node A → Node B
```

---

### 4. START

`START` represents the beginning of graph execution.

```text
START → Node
```

---

### 5. END

`END` represents the termination of graph execution.

```text
Node → END
```

---

### 6. Sequential Workflows

Multiple nodes can be executed one after another.

```text
START
  ↓
Node A
  ↓
Node B
  ↓
Node C
  ↓
END
```

---

### 7. Conditional Edges

The graph can choose the next node based on the current state.

```text
             ┌──→ Node A
Condition ───┤
             └──→ Node B
```

---

### 8. Loops

LangGraph can connect nodes back to previous nodes to create iterative workflows.

```text
Node A
  ↓
Condition
  ↓
  ├── Continue → Node A
  │
  └── Complete → END
```

---

# 🛠️ Technologies Used

* **Python 3.x**
* **LangGraph**
* **TypedDict**
* Python Type Hints

---

# 📦 Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project

```bash
cd LangGraph-Fundamentals
```

### 3. Install dependencies

```bash
pip install langgraph
```

Or, if `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run

Each implementation can be executed independently.

### String Workflow

```bash
python app.py
```

### Mathematical Workflow

```bash
python test.py
```

### Iterative Workflow

```bash
python classify.py
```

---

# 📚 Learning Outcomes

After completing this repository, you will understand:

* What LangGraph is
* How state works in LangGraph
* How to define state using `TypedDict`
* How to create graph nodes
* How nodes communicate through state
* How to connect nodes using edges
* How `START` and `END` work
* How to create sequential workflows
* How to implement conditional routing
* How to create loops
* How to control workflow termination

---

# 🔄 From Simple Workflow to AI Agents

These examples represent the foundation of more advanced LangGraph applications.

The same concepts can later be used to build:

```text
Simple Graph
     ↓
Stateful Workflow
     ↓
Conditional Workflow
     ↓
Iterative Workflow
     ↓
Tool Calling
     ↓
Multi-Agent System
     ↓
AI Agent
```

For example, an AI agent can use a similar architecture:

```text
             START
               │
               ▼
        ┌───────────────┐
        │ Analyze Query │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │ Decide Action │
        └───────┬───────┘
                │
          ┌─────┴─────┐
          │           │
          ▼           ▼
       Tool Call    LLM Response
          │           │
          └─────┬─────┘
                │
                ▼
              END
```

The fundamental ideas of **state, nodes, edges, conditions, and loops** remain the same.

---

# 🎯 Purpose of This Repository

This repository is created as a **hands-on learning project for understanding LangGraph fundamentals** before moving toward advanced concepts such as:

* LangGraph Agents
* Tool Calling
* Human-in-the-Loop
* Memory
* Multi-Agent Workflows
* RAG with LangGraph
* Agentic RAG
* State Persistence
* Checkpointing
* Advanced Conditional Routing

---

## ⭐ If You Find This Useful

If this repository helped you understand LangGraph fundamentals, consider giving it a ⭐ on GitHub.

---

## 👨‍💻 Author

**Aditya Thakur**

B.Tech Information Technology | Generative AI & Software Development Enthusiast

### Tech Interests

```text
Python • Generative AI • LLMs • RAG • LangGraph
Machine Learning • NLP • Software Development
```
