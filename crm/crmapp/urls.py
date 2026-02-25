from django.contrib import admin
from django.urls import include, path
from .views.user_views import home
from .views.auth_views import register_owner

urlpatterns = [
    path("user/", home, name="user_home"),
    path("register-owner/", register_owner, name="register_owner")
]