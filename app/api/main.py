from fastapi import FastAPI
from pydantic import BaseModel
from app.agent.graph import AgentGraph

app = FastAPI(title="Flight Booking Agent API")
graph = AgentGraph()


class ChatRequest(BaseModel):
    user_id: str
    message: str


@app.post("/chat")
async def chat(req: ChatRequest):
    reply = await graph.invoke(req.user_id, req.message)
    return {"reply": reply}
