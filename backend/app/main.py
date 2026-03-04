from contextlib import asynccontextmanager

from api.routes.auth import router as auth_router
from api.routes.chatbot import router as chatbot_router
from api.routes.projects import router as project_router
from db.base import Base
from db.session import engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        Base.metadata.create_all(bind=engine)
        print("=" * 60)
        print("DB initialized")
        print("=" * 60)
    except Exception as e:
        print("=" * 60)
        print("DB error:", e)
        print("=" * 60)
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for Cloud Run
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/test-pushover")
def test_pushover():
    import os

    import requests

    user = os.environ.get("PUSHOVER_USER", "")
    token = os.environ.get("PUSHOVER_TOKEN", "")
    print(f"DEBUG pushover user={user[:5]}... token={token[:5]}...")
    payload = {"user": user, "token": token, "message": "Test from portfolio backend"}
    r = requests.post(
        "https://api.pushover.net/1/messages.json", data=payload, timeout=5
    )
    return {
        "status": r.status_code,
        "response": r.json(),
        "user_set": bool(user),
        "token_set": bool(token),
    }


app.include_router(auth_router)
app.include_router(project_router)
app.include_router(chatbot_router)


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/health")
def health():
    return {"status": "healthy"}
