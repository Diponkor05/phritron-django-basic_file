
from django.contrib import admin
from django.urls import path,include
from App_Login.views import login
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login),
    path('user/',include("App_users.urls"))
]
