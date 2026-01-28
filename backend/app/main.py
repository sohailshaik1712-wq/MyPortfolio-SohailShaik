from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.auth import router as auth_router
from app.api.routes.projects import router as project_router
from app.db.base import Base
from app.db.session import engine

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Portfolio API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(auth_router)
app.include_router(project_router)


@app.get("/")
def read_root():
    return {"message": "Portfolio API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
