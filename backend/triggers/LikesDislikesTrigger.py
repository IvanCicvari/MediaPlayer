from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
import backend.triggers.LikesDislikesTrigger as LikesDislikesTrigger
from models import Video

Base = declarative_base()

def update_likes_count(mapper, connection, target):
    video_id = target.video_id
    total_likes = connection.execute(func.count().label('TotalLikes')).\
        select_from(LikesDislikesTrigger).\
        where(LikesDislikesTrigger.like_status == 1).\
        where(LikesDislikesTrigger.video_id == video_id).\
        scalar() or 0

    connection.execute(
        Video.__table__.update().
        where(Video.video_id == video_id).
        values(total_likes=total_likes)
    )

    mapper(Video, Video.__table__).\
    add_extension(update_likes_count, invoke_for_load=False, invoke_for_insert=False, invoke_for_update=True)
