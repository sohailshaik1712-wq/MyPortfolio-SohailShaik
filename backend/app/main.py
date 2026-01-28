import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.auth import router as auth_router
from app.api.routes.projects import router as project_router
from app.db.base import Base
from app.db.session import engine

load_dotenv()
# Create tables
Base.metadata.create_all(bind=engine)


app = FastAPI(title="Portfolio API")


# CORS (optional for now)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register routes
app.include_router(auth_router)
app.include_router(project_router)

if __name__ == "__main__":
    # Cloud Run provides the PORT environment variable; default to 8080 for safety
    port = int(os.environ.get("PORT", 8080))
    # 'app' refers to your FastAPI(title="Portfolio API") instance
    # host="0.0.0.0" is REQUIRED for Cloud Run to route traffic to your container
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
