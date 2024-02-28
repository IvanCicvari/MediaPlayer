from sqlalchemy.orm import Session
import models
from PydanticModels import *

# User CRUD

def create_user(db: Session, user: UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.IDUser == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, user: UserBase):
    db_user = db.query(models.User).filter(models.User.IDUser == user_id).first()
    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db.query(models.User).filter(models.User.IDUser == user_id).delete()
    db.commit()

# Video CRUD

def create_video(db: Session, video: VideoBase, user_id: int):
    db_video = models.Video(**video.dict(), user_id=user_id)
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

def get_video(db: Session, video_id: int):
    return db.query(models.Video).filter(models.Video.IDVideo == video_id).first()

def get_videos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Video).offset(skip).limit(limit).all()

def update_video(db: Session, video_id: int, video: VideoCreate):
    db_video = db.query(models.Video).filter(models.Video.IDVideo == video_id).first()
    for key, value in video.dict(exclude_unset=True).items():
        setattr(db_video, key, value)
    db.commit()
    db.refresh(db_video)
    return db_video

def delete_video(db: Session, video_id: int):
    db.query(models.Video).filter(models.Video.IDVideo == video_id).delete()
    db.commit()

# LikesDislikes CRUD

def create_like_dislike(db: Session, like_dislike: LikesDislikesBase, user_id: int, video_id: int):
    db_like_dislike = models.LikesDislikes(**like_dislike.dict(), user_id=user_id, video_id=video_id)
    db.add(db_like_dislike)
    db.commit()
    db.refresh(db_like_dislike)
    return db_like_dislike

def get_like_dislike(db: Session, like_id: int):
    return db.query(models.LikesDislikes).filter(models.LikesDislikes.like_id == like_id).first()

def get_likes_dislikes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.LikesDislikes).offset(skip).limit(limit).all()

def delete_like_dislike(db: Session, like_id: int):
    db.query(models.LikesDislikes).filter(models.LikesDislikes.like_id == like_id).delete()
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
    db_subscription = models.Subscription(**subscription.dict(), subscriber_id=subscriber_id, channel_id=channel_id)
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

def get_subscription(db: Session, subscription_id: int):
    return db.query(models.Subscription).filter(models.Subscription.subscription_id == subscription_id).first()

def get_subscriptions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Subscription).offset(skip).limit(limit).all()

def delete_subscription(db: Session, subscription_id: int):
    db.query(models.Subscription).filter(models.Subscription.subscription_id == subscription_id).delete()
    db.commit()
