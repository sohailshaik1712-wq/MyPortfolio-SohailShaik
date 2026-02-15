from app.api.deps import get_current_admin
from app.crud.project import (
    create_project,
    delete_project,
    get_project,
    get_projects,
    update_project,
)
from app.db.session import SessionLocal
from app.schemas.project import (
    ProjectCreate,
    ProjectResponse,
    ProjectUpdate,
)
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/projects", tags=["Projects"])


# --------------------------------------------------
# DATABASE DEPENDENCY
# --------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --------------------------------------------------
# CREATE PROJECT
# --------------------------------------------------
@router.post(
    "/",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_current_admin)],
)
def add_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
):
    """
    Creates a new project with basic info.
    Matches Pydantic ProjectCreate (uses short_description).
    """
    return create_project(db, project)


# --------------------------------------------------
# LIST ALL PROJECTS
# --------------------------------------------------
@router.get("/", response_model=list[ProjectResponse])
def list_projects(
    db: Session = Depends(get_db),
):
    """Fetches all projects from Neon."""
    return get_projects(db)


# --------------------------------------------------
# GET SINGLE PROJECT
# --------------------------------------------------
@router.get("/{project_id}", response_model=ProjectResponse)
def get_single_project(
    project_id: int,
    db: Session = Depends(get_db),
):
    """Fetches a detailed project view by ID."""
    project = get_project(db, project_id)

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with ID {project_id} not found",
        )

    return project


# --------------------------------------------------
# UPDATE PROJECT (PARTIAL)
# --------------------------------------------------
@router.patch(
    "/{project_id}",
    response_model=ProjectResponse,
    dependencies=[Depends(get_current_admin)],
)
def edit_project(
    project_id: int,
    project: ProjectUpdate,
    db: Session = Depends(get_db),
):
    """
    Updates an existing project.
    Allows for the new 'deep' fields (architecture, learnings, etc.)
    """
    updated_project = update_project(
        db=db,
        project_id=project_id,
        project_update=project,
    )

    if not updated_project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
        )

    return updated_project


# --------------------------------------------------
# DELETE PROJECT
# --------------------------------------------------
@router.delete(
    "/{project_id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_current_admin)],
)
def remove_project(
    project_id: int,
    db: Session = Depends(get_db),
):
    """Permanently deletes a project from Neon."""
    success = delete_project(db=db, project_id=project_id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
        )

    return {"message": "Project deleted successfully"}
