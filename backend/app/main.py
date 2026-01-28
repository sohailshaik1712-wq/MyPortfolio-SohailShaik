import os
from contextlib import asynccontextmanager

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.auth import router as auth_router
from app.api.routes.projects import router as project_router
from app.db.base import Base
from app.db.session import engine

# Load environment variables
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handles startup and shutdown events.
    Moving DB creation here prevents Cloud Run from timing out during deployment.
    """
    try:
        # Create tables if they don't exist
        # This now happens AFTER the server has successfully bound to the port.
        Base.metadata.create_all(bind=engine)
        print("✅ Database initialized and tables created.")
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        # The app remains running so you can check logs or reach health checks

    yield
    # Shutdown logic (if any) goes here


# Initialize FastAPI with the lifespan manager
app = FastAPI(title="Portfolio API", lifespan=lifespan)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(auth_router)
app.include_router(project_router)


# Health check for Google Cloud Run
@app.get("/health")
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    # Get port from environment or default to 8080
    port = int(os.environ.get("PORT", 8080))
    # host="0.0.0.0" is mandatory for Cloud Run
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
