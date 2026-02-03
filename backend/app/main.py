from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db, get_session
from .crud import router as crud_router
from .auth import router as auth_router
from .ai import router as ai_router

app = FastAPI(title="Inventory MVP")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(crud_router, prefix="/products", tags=["products"])
app.include_router(ai_router)

@app.on_event("startup")
def on_startup():
    init_db()