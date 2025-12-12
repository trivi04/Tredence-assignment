from fastapi import APIRouter, HTTPException
import uuid
from app.core.models import GraphCreateReq, GraphRunReq
from app.core.engine import run_graph
from app.storage.memory import GRAPHS, RUNS

router = APIRouter(prefix="/graph")

@router.post("/create")
def create_graph(req: GraphCreateReq):
    graph_id = uuid.uuid4().hex
    start = req.start_node or req.nodes[0]
    GRAPHS[graph_id] = {
        "id": graph_id,
        "nodes": req.nodes,
        "edges": req.edges,
        "start_node": start,
    }
    return {"graph_id": graph_id}

@router.post("/run")
def run(req: GraphRunReq):
    graph = GRAPHS.get(req.graph_id)
    if not graph:
        raise HTTPException(404, "Graph not found")

    run_id = uuid.uuid4().hex
    final, log = run_graph(graph, run_id, req.initial_state)

    return {"run_id": run_id, "final_state": final, "execution_log": log}

@router.get("/state/{run_id}")
def state(run_id: str):
    return RUNS.get(run_id)