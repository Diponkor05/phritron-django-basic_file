from django.urls import path
from .views import homepage,usersid
urlpatterns=[
     path("",homepage),
     path("userId/",usersid)
]