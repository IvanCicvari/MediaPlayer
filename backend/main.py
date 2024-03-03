from fastapi import FastAPI
from fastapi.routing import APIRouter

from Controller.UserController import user_router
from Controller.CommentsController import comments_router
from Controller.GenreController import genre_router
from Controller.LikeDislikeController import likeDislike_router
from Controller.RoleController import role_router
from Controller.SubscriptionController import subscription_router
from Controller.TagController import tag_router
from Controller.UserRolesController import userRole_router
from Controller.VideoController import video_router
from Controller.ViewController import view_router

app = FastAPI()

app.include_router(user_router, prefix="/api")
## app.include_router(comments_router, prefix="/CommentsController")
## app.include_router(genre_router, prefix="/GenreController")
## app.include_router(likeDislike_router, prefix="/LikeDislikeController")
## app.include_router(subscription_router, prefix="/SubscriptionController")
## app.include_router(tag_router, prefix="/TagController")
## app.include_router(userRole_router, prefix="/UserRolesController")
## app.include_router(video_router, prefix="/VideoController")
## app.include_router(view_router, prefix="/ViewController")
## app.include_router(role_router, prefix="/RoleController")
