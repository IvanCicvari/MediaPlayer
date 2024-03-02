from sqlalchemy.orm import Session
import models
from PydanticModels import RoleBase, Role

def create_role(db: Session, role: RoleBase):
    db_role = models.Role(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_role(db: Session, role_id: int):
    return db.query(models.Role).filter(models.Role.role_id == role_id).first()

def get_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Role).offset(skip).limit(limit).all()

def delete_role(db: Session, role_id: int):
    db.query(models.Role).filter(models.Role.role_id == role_id).delete()
    db.commit()
