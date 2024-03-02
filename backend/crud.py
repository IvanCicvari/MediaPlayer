from sqlalchemy.orm import Session
import models
from PydanticModels import *
from sqlalchemy.exc import SQLAlchemyError

# User CRUD


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
    db_user = db.query(models.User).filter(
        models.User.IDUser == user_id).first()

    if db_user:
        # Update only the fields that are provided with non-empty values
        for key, value in user_update.dict(exclude_unset=True).items():
            if value is not None and value != "":
                setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)
        return db_user
    else:
        return None


def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(
        models.User.IDUser == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return {"status": "User deleted successfully"}
    else:
        return None


# Video CRUD

def create_video(db: Session, video: VideoBase, user_id: int):
    try:
        db_video = models.Video(
            title=video.title,
            description=video.description,
            thumbnail_url=video.thumbnail_url,
            video_url=video.video_url,
            duration=video.duration,
            categories=video.categories,
    
        )
        db.add(db_video)
        db.commit()
        db.refresh(db_video)
        return User.from_orm(db_video)
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def get_video(db: Session, video_id: int):
    return db.query(models.Video).filter(models.Video.IDVideo == video_id).first()


def get_videos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Video).offset(skip).limit(limit).all()


def update_video(db: Session, video_id: int, video: VideoCreate):
    db_video = db.query(models.Video).filter(
        models.Video.IDVideo == video_id).first()
    for key, value in video.dict(exclude_unset=True).items():
        if value is not None and value != "":
            setattr(db_video, key, value)
    db.commit()
    db.refresh(db_video)
    return db_video


def delete_video(db: Session, video_id: int):
    db.query(models.Video).filter(models.Video.IDVideo == video_id).delete()
    db.commit()

# LikesDislikes CRUD


def create_like_dislike(db: Session, like_dislike: LikesDislikesBase, user_id: int, video_id: int):
    db_like_dislike = models.LikesDislikes(
        **like_dislike.dict(), user_id=user_id, video_id=video_id)
    db.add(db_like_dislike)
    db.commit()
    db.refresh(db_like_dislike)
    return db_like_dislike


def get_like_dislike(db: Session, like_id: int):
    return db.query(models.LikesDislikes).filter(models.LikesDislikes.like_id == like_id).first()


def get_likes_dislikes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.LikesDislikes).offset(skip).limit(limit).all()


def delete_like_dislike(db: Session, like_id: int):
    db.query(models.LikesDislikes).filter(
        models.LikesDislikes.like_id == like_id).delete()
    db.commit()

# View CRUD


def create_view(db: Session, view: ViewBase, user_id: int, video_id: int):
    db_view = models.View(**view.dict(), user_id=user_id, video_id=video_id)
    db.add(db_view)
    db.commit()
    db.refresh(db_view)
    return db_view


def get_view(db: Session, view_id: int):
    return db.query(models.View).filter(models.View.view_id == view_id).first()


def get_views(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.View).offset(skip).limit(limit).all()


def delete_view(db: Session, view_id: int):
    db.query(models.View).filter(models.View.view_id == view_id).delete()
    db.commit()

# Subscription CRUD


def create_subscription(db: Session, subscription: SubscriptionBase, subscriber_id: int, channel_id: int):
    db_subscription = models.Subscription(
        **subscription.dict(), subscriber_id=subscriber_id, channel_id=channel_id)
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription


def get_subscription(db: Session, subscription_id: int):
    return db.query(models.Subscription).filter(models.Subscription.subscription_id == subscription_id).first()


def get_subscriptions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Subscription).offset(skip).limit(limit).all()


def delete_subscription(db: Session, subscription_id: int):
    db.query(models.Subscription).filter(
        models.Subscription.subscription_id == subscription_id).delete()
    db.commit()

# Comments CRUD

def create_comment(db: Session, comment: CommentBase, user_id: int, video_id: int):
    db_comment = models.Comment(**comment.dict(), user_id=user_id, video_id=video_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_comment(db: Session, comment_id: int):
    return db.query(models.Comment).filter(models.Comment.comment_id == comment_id).first()


def get_comments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Comment).offset(skip).limit(limit).all()


def delete_comment(db: Session, comment_id: int):
    db.query(models.Comment).filter(models.Comment.comment_id == comment_id).delete()
    db.commit()

# Tags CRUD

def create_tag(db: Session, tag: TagBase):
    db_tag = models.Tag(**tag.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def get_tag(db: Session, tag_id: int):
    return db.query(models.Tag).filter(models.Tag.tag_id == tag_id).first()


def get_tags(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Tag).offset(skip).limit(limit).all()


def delete_tag(db: Session, tag_id: int):
    db.query(models.Tag).filter(models.Tag.tag_id == tag_id).delete()
    db.commit()

# Genres CRUD

def create_genre(db: Session, genre: GenreBase):
    db_genre = models.Genre(**genre.dict())
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre


def get_genre(db: Session, genre_id: int):
    return db.query(models.Genre).filter(models.Genre.genre_id == genre_id).first()


def get_genres(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Genre).offset(skip).limit(limit).all()


def delete_genre(db: Session, genre_id: int):
    db.query(models.Genre).filter(models.Genre.genre_id == genre_id).delete()
    db.commit()

# VideoTag CRUD

def create_video_tag(db: Session, video_tag: VideoTagBase):
    db_video_tag = models.VideoTag(**video_tag.dict())
    db.add(db_video_tag)
    db.commit()
    db.refresh(db_video_tag)
    return db_video_tag


def get_video_tag(db: Session, video_id: int, tag_id: int):
    return db.query(models.VideoTag).filter(models.VideoTag.video_id == video_id, models.VideoTag.tag_id == tag_id).first()


def get_video_tags(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.VideoTag).offset(skip).limit(limit).all()


def delete_video_tag(db: Session, video_id: int, tag_id: int):
    db.query(models.VideoTag).filter(models.VideoTag.video_id == video_id, models.VideoTag.tag_id == tag_id).delete()
    db.commit()

# VideoGenre CRUD

def create_video_genre(db: Session, video_genre: VideoGenreBase):
    db_video_genre = models.VideoGenre(**video_genre.dict())
    db.add(db_video_genre)
    db.commit()
    db.refresh(db_video_genre)
    return db_video_genre


def get_video_genre(db: Session, video_id: int, genre_id: int):
    return db.query(models.VideoGenre).filter(models.VideoGenre.video_id == video_id, models.VideoGenre.genre_id == genre_id).first()


def get_video_genres(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.VideoGenre).offset(skip).limit(limit).all()


def delete_video_genre(db: Session, video_id: int, genre_id: int):
    db.query(models.VideoGenre).filter(models.VideoGenre.video_id == video_id, models.VideoGenre.genre_id == genre_id).delete()
    db.commit()

# Role CRUD

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

# UsersRoles CRUD

def create_users_roles(db: Session, users_roles: UsersRolesBase):
    db_users_roles = models.UsersRoles(**users_roles.dict())
    db.add(db_users_roles)
    db.commit()
    db.refresh(db_users_roles)
    return db_users_roles


def get_users_roles(db: Session, user_id: int, role_id: int):
    return db.query(models.UsersRoles).filter(models.UsersRoles.user_id == user_id, models.UsersRoles.role_id == role_id).first()


def get_users_all_roles(db: Session, user_id: int):
    return db.query(models.UsersRoles).filter(models.UsersRoles.user_id == user_id).all()


def delete_users_roles(db: Session, user_id: int, role_id: int):
    db.query(models.UsersRoles).filter(models.UsersRoles.user_id == user_id, models.UsersRoles.role_id == role_id).delete()
    db.commit()
