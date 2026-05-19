from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.providers import AIProvider, OpenAICompatibleProvider

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    system_prompt: str | None = None

class ChatResponse(BaseModel):
    reply: str

provider: AIProvider | None = None

def get_provider() -> AIProvider:
    global provider
    if provider is None:
        provider = OpenAICompatibleProvider()
    return provider

@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    p = get_provider()
    try:
        reply = await p.chat(req.message, req.system_prompt)
        return ChatResponse(reply=reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
