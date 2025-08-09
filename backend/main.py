from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import create_graph

app = FastAPI()

# Add CORS middleware for frontend compatibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    thread_id: str

_agent = None
#_client = None # Uncomment if using MCP client (math server)

async def get_agent():
    """Get or initialize the agent."""
    global _agent
    if _agent is None:
        _agent = await create_graph()  # No unpacking; single return value
    return _agent

@app.post("/chat")
async def chat(request: ChatRequest):
    agent = await get_agent()
    config = {"configurable": {"thread_id": request.thread_id}}
    response = await agent.ainvoke({"messages": [{"role": "user", "content": request.message}]}, config)
    return {"reply": response["messages"][-1].content}