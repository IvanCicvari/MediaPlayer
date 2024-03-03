from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from PydanticModels import *
from Repository.RoleRepository import *
from database import SessionLocal

role_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CRUD operations for Roles
@role_router.post("/roles/", tags=["Roles"])
def create_role_api(role: RoleCreate, db: Session = Depends(get_db)):
    return create_role(db, role)

@role_router.get("/roles/{role_id}", tags=["Roles"])
def read_role_api(role_id: int, db: Session = Depends(get_db)):
    db_role = get_role(db, role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@role_router.get("/roles/", tags=["Roles"])
def read_roles_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_roles(db, skip=skip, limit=limit)

@role_router.delete("/roles/{role_id}", tags=["Roles"])
def delete_role_api(role_id: int, db: Session = Depends(get_db)):
    db_role = delete_role(db, role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role
