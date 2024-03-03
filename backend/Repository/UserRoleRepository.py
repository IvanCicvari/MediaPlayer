from sqlalchemy.orm import Session
from Models import UsersRolesModel
from PydanticModels import UsersRolesBase, UsersRoles

def create_users_roles(db: Session, users_roles: UsersRolesBase):
    db_users_roles = UsersRolesModel.UsersRoles(**users_roles.dict())
    db.add(db_users_roles)
    db.commit()
    db.refresh(db_users_roles)
    return db_users_roles

def get_users_roles(db: Session, user_id: int, role_id: int):
    return db.query(UsersRolesModel.UsersRoles).filter(UsersRolesModel.UsersRoles.user_id == user_id, UsersRolesModel.UsersRoles.role_id == role_id).first()

def get_users_all_roles(db: Session, user_id: int):
    return db.query(UsersRolesModel.UsersRoles).filter(UsersRolesModel.UsersRoles.user_id == user_id).all()

def delete_users_roles(db: Session, user_id: int, role_id: int):
    db.query(UsersRolesModel.UsersRoles).filter(UsersRolesModel.UsersRoles.user_id == user_id, UsersRolesModel.UsersRoles.role_id == role_id).delete()
    db.commit()
