from app.db.base import Base
from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    tech_stack = Column(String(300))
    github_url = Column(String(300))
    live_url = Column(String(300))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
