from django.urls import include
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
]
