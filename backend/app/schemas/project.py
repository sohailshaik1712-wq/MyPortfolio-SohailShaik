from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ProjectBase(BaseModel):
    title: str
    short_description: str
    tech_stack: Optional[str] = None
    github_url: Optional[str] = None
    live_url: Optional[str] = None


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    short_description: Optional[str] = None

    problem_statement: Optional[str] = None
    why_built: Optional[str] = None
    architecture: Optional[str] = None
    implementation_details: Optional[str] = None
    challenges: Optional[str] = None
    learnings: Optional[str] = None
    future_improvements: Optional[str] = None

    tech_stack: Optional[str] = None
    github_url: Optional[str] = None
    live_url: Optional[str] = None


class ProjectResponse(ProjectBase):
    id: int
    created_at: datetime

    # Extended fields appear in response
    problem_statement: Optional[str] = None
    why_built: Optional[str] = None
    architecture: Optional[str] = None
    implementation_details: Optional[str] = None
    challenges: Optional[str] = None
    learnings: Optional[str] = None
    future_improvements: Optional[str] = None

    class Config:
        from_attributes = True
