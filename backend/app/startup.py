from app.db.base import Base
from app.db.session import engine


def init_db():
    """Initialize database tables"""
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    print("Initializing database...")
    init_db()
    print("Database initialized successfully!")
