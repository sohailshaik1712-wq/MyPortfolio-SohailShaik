from app.models.project import Project
from app.schemas.project import ProjectCreate
from sqlalchemy.orm import Session


def create_project(db: Session, project: ProjectCreate):
    db_project = Project(**project.dict())

    db.add(db_project)
    db.commit()
    db.refresh(db_project)

    return db_project


def get_projects(db: Session):
    return db.query(Project).all()


def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()


def update_project(db: Session, project_id: int, project_update: ProjectCreate):
    db_project = db.query(Project).filter(Project.id == project_id).first()
    if db_project:
        # Dynamically update attributes based on the schema
        for key, value in project_update.dict().items():
            setattr(db_project, key, value)

        db.commit()
        db.refresh(db_project)
    return db_project


def delete_project(db: Session, project_id: int):
    db_project = db.query(Project).filter(Project.id == project_id).first()
    if db_project:
        db.delete(db_project)
        db.commit()
        return True
    return False
