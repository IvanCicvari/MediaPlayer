from sqlalchemy.orm import Session
import Models
from PydanticModels import GenreBase, Genre

def create_genre(db: Session, genre: GenreBase):
    db_genre = Models.Genre(**genre.dict())
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre

def get_genre(db: Session, genre_id: int):
    return db.query(Models.Genre).filter(Models.Genre.genre_id == genre_id).first()

def get_genres(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Models.Genre).offset(skip).limit(limit).all()

def delete_genre(db: Session, genre_id: int):
    db.query(Models.Genre).filter(Models.Genre.genre_id == genre_id).delete()
    db.commit()
