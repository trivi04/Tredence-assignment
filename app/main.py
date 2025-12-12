from fastapi import FastAPI
from app.api.graph_routes import router
import app.workflows.summarization

app = FastAPI(title="Agent Workflow Engine")
app.include_router(router)