from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from PydanticModels import *
from Repository.UserRoleRepository import *
from database import SessionLocal

userRole_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD operations for UsersRoles
@userRole_router.post("/users-roles/", tags=["UsersRoles"])
def create_users_roles_api(users_roles: UsersRolesCreate, db: Session = Depends(get_db)):
    return create_users_roles(db, users_roles)

@userRole_router.get("/users-roles/{users_roles_id}", tags=["UsersRoles"])
def read_users_roles_api(users_roles_id: int, db: Session = Depends(get_db)):
    db_users_roles = get_users_roles(db, users_roles_id)
    if db_users_roles is None:
        raise HTTPException(status_code=404, detail="UsersRoles not found")
    return db_users_roles

@userRole_router.get("/users-roles/", tags=["UsersRoles"])
def read_users_all_roles_api(user_id: int, db: Session = Depends(get_db)):
    return get_users_all_roles(db, user_id)

@userRole_router.delete("/users-roles/{users_roles_id}", tags=["UsersRoles"])
def delete_users_roles_api(users_roles_id: int, db: Session = Depends(get_db)):
    db_users_roles = delete_users_roles(db, users_roles_id)
    if db_users_roles is None:
        raise HTTPException(status_code=404, detail="UsersRoles not found")
    return db_users_roles
