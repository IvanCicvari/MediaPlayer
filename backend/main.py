from fastapi import FastAPI, HTTPException, Depends, Path
from sqlalchemy.orm import Session
from crud import create_user, get_user, get_users, update_user, delete_user, create_video, get_video, get_videos, update_video, delete_video, create_like_dislike, get_like_dislike, get_likes_dislikes, delete_like_dislike, create_view, get_view, get_views, delete_view, create_subscription, get_subscription, get_subscriptions, delete_subscription
from PydanticModels import *
from models import User, Video, LikesDislikes, View, Subscription
from database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_id_path_parameter(user_id: int = Path(..., title="User ID")):
    return user_id

def get_video_id_path_parameter(video_id: int = Path(..., title="Video ID")):
    return video_id

# Root route
@app.get('/', tags=["Root"])
def get_home():
    return {"message": "Welcome to your API. Explore the documentation at /docs."}

# CRUD operations for Users
@app.post("/users/")
def create_user_api(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@app.get("/users/{user_id}")
def read_user_api(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}")
def update_user_api(user_id: int, user: UserBase, db: Session = Depends(get_db)):
    db_user = update_user(db, user_id, user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}")
def delete_user_api(user_id: int, db: Session = Depends(get_db)):
    db_user = delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# CRUD operations for Videos
@app.post("/videos/")
def create_video_api(video: VideoCreate, user_id: int, db: Session = Depends(get_db)):
    return create_video(db, video, user_id)

@app.get("/videos/{video_id}")
def read_video_api(video_id: int, db: Session = Depends(get_db)):
    db_video = get_video(db, video_id)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video

@app.get("/videos/")
def read_videos_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_videos(db, skip=skip, limit=limit)

@app.put("/videos/{video_id}")
def update_video_api(video_id: int, video: VideoCreate, db: Session = Depends(get_db)):
    db_video = update_video(db, video_id, video)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video

@app.delete("/videos/{video_id}")
def delete_video_api(video_id: int, db: Session = Depends(get_db)):
    db_video = delete_video(db, video_id)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video


# CRUD operations for Likes/Dislikes
@app.post("/likes-dislikes/")
def create_like_dislike_api(like_dislike: LikesDislikesCreate, user_id: int, video_id: int, db: Session = Depends(get_db)):
    return create_like_dislike(db, like_dislike, user_id, video_id)

@app.get("/likes-dislikes/{like_id}")
def read_like_dislike_api(like_id: int, db: Session = Depends(get_db)):
    db_like_dislike = get_like_dislike(db, like_id)
    if db_like_dislike is None:
        raise HTTPException(status_code=404, detail="Like/Dislike not found")
    return db_like_dislike

@app.get("/likes-dislikes/")
def read_likes_dislikes_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_likes_dislikes(db, skip=skip, limit=limit)

@app.delete("/likes-dislikes/{like_id}")
def delete_like_dislike_api(like_id: int, db: Session = Depends(get_db)):
    db_like_dislike = delete_like_dislike(db, like_id)
    if db_like_dislike is None:
        raise HTTPException(status_code=404, detail="Like/Dislike not found")
    return db_like_dislike

# CRUD operations for Views
@app.post("/views/")
def create_view_api(view: ViewCreate, user_id: int, video_id: int, db: Session = Depends(get_db)):
    return create_view(db, view, user_id, video_id)

@app.get("/views/{view_id}")
def read_view_api(view_id: int, db: Session = Depends(get_db)):
    db_view = get_view(db, view_id)
    if db_view is None:
        raise HTTPException(status_code=404, detail="View not found")
    return db_view

@app.get("/views/")
def read_views_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_views(db, skip=skip, limit=limit)

@app.delete("/views/{view_id}")
def delete_view_api(view_id: int, db: Session = Depends(get_db)):
    db_view = delete_view(db, view_id)
    if db_view is None:
        raise HTTPException(status_code=404, detail="View not found")
    return db_view


# CRUD operations for Subscriptions
@app.post("/subscriptions/")
def create_subscription_api(subscription: SubscriptionCreate, subscriber_id: int, channel_id: int, db: Session = Depends(get_db)):
    return create_subscription(db, subscription, subscriber_id, channel_id)


@app.get("/subscriptions/{subscription_id}")
def read_subscription_api(subscription_id: int, db: Session = Depends(get_db)):
    db_subscription = get_subscription(db, subscription_id)
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_subscription

@app.get("/subscriptions/")
def read_subscriptions_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_subscriptions(db, skip=skip, limit=limit)

@app.delete("/subscriptions/{subscription_id}")
def delete_subscription_api(subscription_id: int, db: Session = Depends(get_db)):
    db_subscription = delete_subscription(db, subscription_id)
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_subscription