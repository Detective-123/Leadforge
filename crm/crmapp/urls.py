from django.contrib import admin
from django.urls import include, path
from .views.user_views import home

urlpatterns = [
    path("user/", home, name="user_home"),
]