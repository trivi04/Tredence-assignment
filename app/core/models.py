from pydantic import BaseModel
from typing import Dict, List, Optional, Any

class GraphCreateReq(BaseModel):
    nodes: List[str]
    edges: Dict[str, str] = {}
    start_node: Optional[str] = None

class GraphRunReq(BaseModel):
    graph_id: str
    initial_state: Dict[str, Any] = {}