from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
from sqlalchemy.orm import mapper

from models import Video, View

def update_views_count(mapper, connection, target):
    video_id = target.video_id
    total_views = connection.execute(func.count().label('TotalViews')).\
        select_from(View).\
        where(View.video_id == video_id).\
        scalar() or 0

    connection.execute(
        Video.__table__.update().
        where(Video.video_id == video_id).
        values(total_views=total_views)
    )

mapper(View, View.__table__).\
    add_extension(update_views_count, invoke_for_load=False, invoke_for_insert=True, invoke_for_update=False)
