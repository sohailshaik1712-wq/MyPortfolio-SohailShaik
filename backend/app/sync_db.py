from db.base import Base
from db.session import engine
from models.project import Project  # Ensure model is imported


def reset_db():
    print("Dropping and recreating tables in Neon...")
    # WARNING: This deletes all data in the projects table!
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("✅ Sync complete! Your Neon table now matches your Python model.")


if __name__ == "__main__":
    reset_db()
