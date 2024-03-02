from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from crud import *
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

# Root route
@app.get('/', tags=["Root"])
def get_home():
    return {"message": "Welcome to your API. Explore the documentation at /docs."}

# CRUD operations for Users
@app.post("/users/", tags=["Users"])
def create_user_api(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@app.get("/users/{user_id}", tags=["Users"])
def read_user_api(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", tags=["Users"])
def update_user_api(user_id: int, user: UserBase, db: Session = Depends(get_db)):
    db_user = update_user(db, user_id, user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}", tags=["Users"], response_model=dict)
def delete_user_api(user_id: int, db: Session = Depends(get_db)):
    db_user = delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"status": "User deleted successfully"}

# CRUD operations for Videos
@app.post("/videos/", tags=["Videos"])
def create_video_api(video: VideoCreate, user_id: int, db: Session = Depends(get_db)):
    return create_video(db, video, user_id)

@app.get("/videos/{video_id}", tags=["Videos"])
def read_video_api(video_id: int, db: Session = Depends(get_db)):
    db_video = get_video(db, video_id)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video

@app.get("/videos/", tags=["Videos"])
def read_videos_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_videos(db, skip=skip, limit=limit)

@app.put("/videos/{video_id}", tags=["Videos"])
def update_video_api(video_id: int, video: VideoCreate, db: Session = Depends(get_db)):
    db_video = update_video(db, video_id, video)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video

@app.delete("/videos/{video_id}", tags=["Videos"])
def delete_video_api(video_id: int, db: Session = Depends(get_db)):
    db_video = delete_video(db, video_id)
    if db_video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return db_video

# CRUD operations for Likes/Dislikes
@app.post("/likes-dislikes/", tags=["Likes/Dislikes"])
def create_like_dislike_api(like_dislike: LikesDislikesCreate, user_id: int, video_id: int, db: Session = Depends(get_db)):
    return create_like_dislike(db, like_dislike, user_id, video_id)

@app.get("/likes-dislikes/{like_id}", tags=["Likes/Dislikes"])
def read_like_dislike_api(like_id: int, db: Session = Depends(get_db)):
    db_like_dislike = get_like_dislike(db, like_id)
    if db_like_dislike is None:
        raise HTTPException(status_code=404, detail="Like/Dislike not found")
    return db_like_dislike

@app.get("/likes-dislikes/", tags=["Likes/Dislikes"])
def read_likes_dislikes_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_likes_dislikes(db, skip=skip, limit=limit)

@app.delete("/likes-dislikes/{like_id}", tags=["Likes/Dislikes"])
def delete_like_dislike_api(like_id: int, db: Session = Depends(get_db)):
    db_like_dislike = delete_like_dislike(db, like_id)
    if db_like_dislike is None:
        raise HTTPException(status_code=404, detail="Like/Dislike not found")
    return db_like_dislike

# CRUD operations for Views
@app.post("/views/", tags=["Views"])
def create_view_api(view: ViewCreate, user_id: int, video_id: int, db: Session = Depends(get_db)):
    return create_view(db, view, user_id, video_id)

@app.get("/views/{view_id}", tags=["Views"])
def read_view_api(view_id: int, db: Session = Depends(get_db)):
    db_view = get_view(db, view_id)
    if db_view is None:
        raise HTTPException(status_code=404, detail="View not found")
    return db_view

@app.get("/views/", tags=["Views"])
def read_views_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_views(db, skip=skip, limit=limit)

@app.delete("/views/{view_id}", tags=["Views"])
def delete_view_api(view_id: int, db: Session = Depends(get_db)):
    db_view = delete_view(db, view_id)
    if db_view is None:
        raise HTTPException(status_code=404, detail="View not found")
    return db_view

# CRUD operations for Subscriptions
@app.post("/subscriptions/", tags=["Subscriptions"])
def create_subscription_api(subscription: SubscriptionCreate, subscriber_id: int, channel_id: int, db: Session = Depends(get_db)):
    return create_subscription(db, subscription, subscriber_id, channel_id)

@app.get("/subscriptions/{subscription_id}", tags=["Subscriptions"])
def read_subscription_api(subscription_id: int, db: Session = Depends(get_db)):
    db_subscription = get_subscription(db, subscription_id)
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_subscription

@app.get("/subscriptions/", tags=["Subscriptions"])
def read_subscriptions_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_subscriptions(db, skip=skip, limit=limit)

@app.delete("/subscriptions/{subscription_id}", tags=["Subscriptions"])
def delete_subscription_api(subscription_id: int, db: Session = Depends(get_db)):
    db_subscription = delete_subscription(db, subscription_id)
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return db_subscription

# CRUD operations for Comments
@app.post("/comments/", tags=["Comments"])
def create_comment_api(comment: CommentCreate, user_id: int, video_id: int, db: Session = Depends(get_db)):
    return create_comment(db, comment, user_id, video_id)

@app.get("/comments/{comment_id}", tags=["Comments"])
def read_comment_api(comment_id: int, db: Session = Depends(get_db)):
    db_comment = get_comment(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@app.get("/comments/", tags=["Comments"])
def read_comments_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_comments(db, skip=skip, limit=limit)

@app.delete("/comments/{comment_id}", tags=["Comments"])
def delete_comment_api(comment_id: int, db: Session = Depends(get_db)):
    db_comment = delete_comment(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

# CRUD operations for Tags
@app.post("/tags/", tags=["Tags"])
def create_tag_api(tag: TagCreate, db: Session = Depends(get_db)):
    return create_tag(db, tag)

@app.get("/tags/{tag_id}", tags=["Tags"])
def read_tag_api(tag_id: int, db: Session = Depends(get_db)):
    db_tag = get_tag(db, tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag

@app.get("/tags/", tags=["Tags"])
def read_tags_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_tags(db, skip=skip, limit=limit)

@app.delete("/tags/{tag_id}", tags=["Tags"])
def delete_tag_api(tag_id: int, db: Session = Depends(get_db)):
    db_tag = delete_tag(db, tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag

# CRUD operations for Genres
@app.post("/genres/", tags=["Genres"])
def create_genre_api(genre: GenreCreate, db: Session = Depends(get_db)):
    return create_genre(db, genre)

@app.get("/genres/{genre_id}", tags=["Genres"])
def read_genre_api(genre_id: int, db: Session = Depends(get_db)):
    db_genre = get_genre(db, genre_id)
    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre

@app.get("/genres/", tags=["Genres"])
def read_genres_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_genres(db, skip=skip, limit=limit)

@app.delete("/genres/{genre_id}", tags=["Genres"])
def delete_genre_api(genre_id: int, db: Session = Depends(get_db)):
    db_genre = delete_genre(db, genre_id)
    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre

# CRUD operations for VideoTags
@app.post("/video-tags/", tags=["VideoTags"])
def create_video_tag_api(video_tag: VideoTagCreate, db: Session = Depends(get_db)):
    return create_video_tag(db, video_tag)

@app.get("/video-tags/{video_tag_id}", tags=["VideoTags"])
def read_video_tag_api(video_tag_id: int, db: Session = Depends(get_db)):
    db_video_tag = get_video_tag(db, video_tag_id)
    if db_video_tag is None:
        raise HTTPException(status_code=404, detail="VideoTag not found")
    return db_video_tag

@app.get("/video-tags/", tags=["VideoTags"])
def read_video_tags_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_video_tags(db, skip=skip, limit=limit)

@app.delete("/video-tags/{video_tag_id}", tags=["VideoTags"])
def delete_video_tag_api(video_tag_id: int, db: Session = Depends(get_db)):
    db_video_tag = delete_video_tag(db, video_tag_id)
    if db_video_tag is None:
        raise HTTPException(status_code=404, detail="VideoTag not found")
    return db_video_tag

# CRUD operations for VideoGenres
@app.post("/video-genres/", tags=["VideoGenres"])
def create_video_genre_api(video_genre: VideoGenreCreate, db: Session = Depends(get_db)):
    return create_video_genre(db, video_genre)

@app.get("/video-genres/{video_genre_id}", tags=["VideoGenres"])
def read_video_genre_api(video_genre_id: int, db: Session = Depends(get_db)):
    db_video_genre = get_video_genre(db, video_genre_id)
    if db_video_genre is None:
        raise HTTPException(status_code=404, detail="VideoGenre not found")
    return db_video_genre

@app.get("/video-genres/", tags=["VideoGenres"])
def read_video_genres_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_video_genres(db, skip=skip, limit=limit)

@app.delete("/video-genres/{video_genre_id}", tags=["VideoGenres"])
def delete_video_genre_api(video_genre_id: int, db: Session = Depends(get_db)):
    db_video_genre = delete_video_genre(db, video_genre_id)
    if db_video_genre is None:
        raise HTTPException(status_code=404, detail="VideoGenre not found")
    return db_video_genre

# CRUD operations for Roles
@app.post("/roles/", tags=["Roles"])
def create_role_api(role: RoleCreate, db: Session = Depends(get_db)):
    return create_role(db, role)

@app.get("/roles/{role_id}", tags=["Roles"])
def read_role_api(role_id: int, db: Session = Depends(get_db)):
    db_role = get_role(db, role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@app.get("/roles/", tags=["Roles"])
def read_roles_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_roles(db, skip=skip, limit=limit)

@app.delete("/roles/{role_id}", tags=["Roles"])
def delete_role_api(role_id: int, db: Session = Depends(get_db)):
    db_role = delete_role(db, role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

# CRUD operations for UsersRoles
@app.post("/users-roles/", tags=["UsersRoles"])
def create_users_roles_api(users_roles: UsersRolesCreate, db: Session = Depends(get_db)):
    return create_users_roles(db, users_roles)

@app.get("/users-roles/{users_roles_id}", tags=["UsersRoles"])
def read_users_roles_api(users_roles_id: int, db: Session = Depends(get_db)):
    db_users_roles = get_users_roles(db, users_roles_id)
    if db_users_roles is None:
        raise HTTPException(status_code=404, detail="UsersRoles not found")
    return db_users_roles

@app.get("/users-roles/", tags=["UsersRoles"])
def read_users_all_roles_api(user_id: int, db: Session = Depends(get_db)):
    return get_users_all_roles(db, user_id)

@app.delete("/users-roles/{users_roles_id}", tags=["UsersRoles"])
def delete_users_roles_api(users_roles_id: int, db: Session = Depends(get_db)):
    db_users_roles = delete_users_roles(db, users_roles_id)
    if db_users_roles is None:
        raise HTTPException(status_code=404, detail="UsersRoles not found")
    return db_users_roles
