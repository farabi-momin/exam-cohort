from django.urls import include
from django.urls import path
from . import views
from django.contrib.auth.models import User
from rest_framework import routers
from api import views

userrouter = routers.DefaultRouter()
userrouter.register(r'User',views.UserViewSet)

urlpatterns = [
    path('', include(userrouter.urls)),
]
