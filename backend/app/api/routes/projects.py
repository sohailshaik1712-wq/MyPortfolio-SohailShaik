from app.api.deps import get_current_admin
from app.crud.project import (
    create_project,
    delete_project,
    get_projects,
    update_project,
)
from app.db.session import SessionLocal
from app.schemas.project import ProjectCreate, ProjectResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/projects", tags=["Projects"])


# Dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post(
    "/", response_model=ProjectResponse, dependencies=[Depends(get_current_admin)]
)
def add_project(project: ProjectCreate, db: Session = Depends(get_db)):
    return create_project(db, project)


@router.get("/", response_model=list[ProjectResponse])
def list_projects(db: Session = Depends(get_db)):
    return get_projects(db)


@router.put("/{project_id}")
def edit_project(
    project_id: int,
    project: ProjectCreate,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin),
):
    return update_project(db=db, project_id=project_id, project_update=project)


@router.delete("/{project_id}")
def remove_project(
    project_id: int, db: Session = Depends(get_db), admin=Depends(get_current_admin)
):
    success = delete_project(db=db, project_id=project_id)
    if not success:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project deleted"}
