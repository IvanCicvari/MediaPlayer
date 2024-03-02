# PydanticModels.py

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel

# User Models


class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    profile_image: Optional[str] = None
    bio: Optional[str] = None
    subscription_status: str


class UserCreate(UserBase):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    profile_image: str
    bio: str
    subscription_status: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    profile_image: Optional[str] = None
    bio: Optional[str] = None
    subscription_status: Optional[str] = None

    class Config:
        orm_mode = True


class User(UserBase):
    IDUser: int
    created_at: datetime
    last_login: Optional[datetime]
    is_verified: bool
    subscription_status: str
    videos: List['Video'] = []
    likes: List['LikesDislikes'] = []
    views: List['View'] = []
    subscriptions: List['Subscription'] = []

    class Config:
        orm_mode = True

# Video Models


class VideoBase(BaseModel):
    title: str
    description: str
    upload_date: datetime
    thumbnail_url: str
    video_url: str
    duration: Optional[int]
    categories: str
    privacy_setting: str
    total_likes: int = 0
    total_views: int = 0
    total_subscribers: int = 0


class VideoCreate(VideoBase):
    title: str
    description: str
    thumbnail_url: str
    video_url: str
    duration: Optional[int]
    categories: str
    class Config:
        orm_mode = True


class Video(VideoBase):
    IDVideo: int
    user_id: int
    user: User
    views: List['View'] = []
    likes: List['LikesDislikes'] = []

    class Config:
        orm_mode = True

# LikesDislikes Models


class LikesDislikesBase(BaseModel):
    user_id: int
    video_id: int
    like_status: int


class LikesDislikesCreate(LikesDislikesBase):
    pass


class LikesDislikes(LikesDislikesBase):
    like_id: int
    user: User
    video: Video

    class Config:
        orm_mode = True

# View Models


class ViewBase(BaseModel):
    user_id: int
    video_id: int
    view_date: datetime


class ViewCreate(ViewBase):
    pass


class View(ViewBase):
    view_id: int
    user: User
    video: Video

    class Config:
        orm_mode = True

# Subscription Models


class SubscriptionBase(BaseModel):
    subscriber: int
    channel: int


class SubscriptionCreate(SubscriptionBase):
    pass


class Subscription(SubscriptionBase):
    subscription_id: int
    subscriber: User
    channel: User

    class Config:
        orm_mode = True
from typing import List
from datetime import datetime
from pydantic import BaseModel

# Comment Models
class CommentBase(BaseModel):
    user_id: int
    video_id: int
    comment_text: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    comment_id: int
    comment_date: datetime
    user: 'User'
    video: 'Video'

    class Config:
        orm_mode = True

# Tag Models
class TagBase(BaseModel):
    tag_name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    tag_id: int

    class Config:
        orm_mode = True

# Genre Models
class GenreBase(BaseModel):
    genre_name: str

class GenreCreate(GenreBase):
    pass

class Genre(GenreBase):
    genre_id: int

    class Config:
        orm_mode = True

# VideoTag Models
class VideoTagBase(BaseModel):
    video_id: int
    tag_id: int

class VideoTagCreate(VideoTagBase):
    pass

class VideoTag(VideoTagBase):
    class Config:
        orm_mode = True

# VideoGenre Models
class VideoGenreBase(BaseModel):
    video_id: int
    genre_id: int

class VideoGenreCreate(VideoGenreBase):
    pass

class VideoGenre(VideoGenreBase):
    class Config:
        orm_mode = True

# Role Models
class RoleBase(BaseModel):
    role_name: str

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    role_id: int

    class Config:
        orm_mode = True

# UsersRoles Models
class UsersRolesBase(BaseModel):
    user_id: int
    role_id: int

class UsersRolesCreate(UsersRolesBase):
    pass

class UsersRoles(UsersRolesBase):
    class Config:
        orm_mode = True




