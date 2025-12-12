Agent Workflow Engine – (with the implementation of option B:Summarization & Refinement)

This project implements a minimal graph-based agent workflow engine using FastAPI.
It supports nodes, state passing, conditional branching, and looping. A rule-based
text summarization + refinement workflow is included.

How To Run

make a vitual environment and initialize a virtual environment
python3 -m venv vm
vm\Scripts\activate

Use this command to install the required libraries:
pip install -r requirements.txt

Then finally run the api using the command below:
uvicorn app.main:app --reload


Open API docs:
http://127.0.0.1:8000/docs


The workflow engine supports the following:
1. Graph-based execution  
2. Shared state dictionary  
3. Sequential transitions via edges  
4. Conditional branching via thresholds defined 
5. Looping and Execution logs  
6. In-memory storage as well

Things I would improve if I had more time:

1. I would implement a asynchrnous backgroud for execution of the tasks

2. A small and interactive UI to visualize and for ease of use"# Tredence-assignment" 
