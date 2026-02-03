from fastapi import APIRouter, HTTPException, Depends, Form
from pydantic import BaseModel
import os
import jwt
from datetime import datetime, timedelta

router = APIRouter()

JWT_SECRET = os.getenv("JWT_SECRET", "replace_this_with_a_secret")
ADMIN_USER = os.getenv("ADMIN_USER", "admin")
ADMIN_PASS = os.getenv("ADMIN_PASS", "contraseña")

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

@router.post("/token", response_model=Token)
def login(username: str = Form(...), password: str = Form(...)):
    if username != ADMIN_USER or password != ADMIN_PASS:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=12)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return {"access_token": token}