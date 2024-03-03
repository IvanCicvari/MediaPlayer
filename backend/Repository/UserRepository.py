from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import Models as models
from PydanticModels import UserCreate, UserUpdate, User

def create_user(db: Session, user: UserCreate) -> User:
    try:
        db_user = models.User(
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            email=user.email,
            password=user.password,
            profile_image=user.profile_image,
            bio=user.bio,
            subscription_status=user.subscription_status,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return User.from_orm(db_user)
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.IDUser == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, user_update: UserUpdate):
    db_user = db.query(models.User).filter(models.User.IDUser == user_id).first()

    if db_user:
        for key, value in user_update.dict(exclude_unset=True).items():
            if value is not None and value != "":
                setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)
        return db_user
    else:
        return None

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.IDUser == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return {"status": "User deleted successfully"}
    else:
        return None
