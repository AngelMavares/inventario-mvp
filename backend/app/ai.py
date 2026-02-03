# Endpoint opcional de ejemplo que usa OpenAI para una respuesta rápida sobre inventario.
# Requiere la variable de entorno OPENAI_API_KEY para activarse.
from fastapi import APIRouter, HTTPException, Body
import os
import openai

router = APIRouter(prefix="/ai", tags=["ai"])

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_KEY:
    openai.api_key = OPENAI_KEY

@router.post("/ask")
def ask_ai(payload: dict = Body(...)):
    question = payload.get("question")
    if not OPENAI_KEY:
        raise HTTPException(status_code=400, detail="OPENAI_API_KEY no configurada")
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content": question}],
        max_tokens=300
    )
    return {"answer": resp.choices[0].message.content}