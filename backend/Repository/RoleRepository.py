from sqlalchemy.orm import Session
from Models import RoleModel  # Replace 'Models' with the actual module name
from PydanticModels import RoleBase

def create_role(db: Session, role: RoleBase):
    db_role = RoleModel(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_role(db: Session, role_id: int):
    return db.query(RoleModel).filter(RoleModel.role_id == role_id).first()

def get_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(RoleModel).offset(skip).limit(limit).all()

def delete_role(db: Session, role_id: int):
    db.query(RoleModel).filter(RoleModel.role_id == role_id).delete()
    db.commit()
