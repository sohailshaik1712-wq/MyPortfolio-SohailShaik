from app.db.base import Base
from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    short_description = Column(Text, nullable=False)

    # Detailed fields
    problem_statement = Column(Text)
    why_built = Column(Text)
    architecture = Column(Text)
    implementation_details = Column(Text)
    challenges = Column(Text)
    learnings = Column(Text)
    future_improvements = Column(Text)

    tech_stack = Column(String(300))
    github_url = Column(String(300))
    live_url = Column(String(300))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
