from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate
from sqlalchemy.orm import Session


def create_project(db: Session, project: ProjectCreate):
    db_project = Project(**project.model_dump())

    db.add(db_project)
    db.commit()
    db.refresh(db_project)

    return db_project


def get_projects(db: Session):
    return db.query(Project).all()


def get_project(db: Session, project_id: int):
    return db.get(Project, project_id)


def update_project(db: Session, project_id: int, project_update: ProjectUpdate):

    db_project = db.query(Project).filter(Project.id == project_id).first()

    if not db_project:
        return None

    update_data = project_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_project, key, value)

    db.commit()
    db.refresh(db_project)

    return db_project


def delete_project(db: Session, project_id: int):

    db_project = db.query(Project).filter(Project.id == project_id).first()

    if not db_project:
        return False

    db.delete(db_project)
    db.commit()

    return True
