from fastapi import FastAPI
from agents.qwen_agent import Qwen3Agent
import uvicorn
import os

app = FastAPI(title="Qwen-Agent API")
agent = Qwen3Agent()

@app.post("/task")
async def run_agent_task(query: str):
    """Run complex multi-step task with context handling"""
    result = agent.run_task(query)
    return {"result": result}

@app.get("/memory")
async def get_memory_summary():
    """Get current context summary"""
    return {"summary": agent.memory.summary}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
