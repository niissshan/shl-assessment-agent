from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from agent import chat_with_agent

app = FastAPI()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


@app.get("/health")
def health():

    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):

    messages = []

    for msg in request.messages:

        messages.append({
            "role": msg.role,
            "content": msg.content
        })

    response = chat_with_agent(messages)

    return response