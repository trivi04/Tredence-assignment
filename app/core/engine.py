import time
from app.core.registry import NODE_REGISTRY, TOOLS
from app.storage.memory import RUNS

def run_graph(graph: dict, run_id: str, initial_state: dict):
    current = graph["start_node"]
    state = dict(initial_state)
    log = []

    RUNS[run_id] = {
        "id": run_id,
        "graph_id": graph["id"],
        "status": "running",
        "state": state,
        "log": log,
        "started_at": time.time(),
    }

    while current:
        node_fn = NODE_REGISTRY[current]
        state = node_fn(state, TOOLS) or state
        log.append(current)

        RUNS[run_id]["state"] = state
        RUNS[run_id]["log"] = log

        if state.get("_terminate"):
            break

        if state.get("_next"):
            current = state.pop("_next")
        else:
            current = graph["edges"].get(current)

    RUNS[run_id]["status"] = "completed"
    RUNS[run_id]["ended_at"] = time.time()

    return state, log