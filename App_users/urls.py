from django.urls import path
from .views import homepage,usersid,userid
urlpatterns=[
     path("",homepage),
     path("userId/",usersid),
     path("userid/<int:id>",userid)
]