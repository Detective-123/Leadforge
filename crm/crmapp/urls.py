from django.contrib import admin
from django.urls import include, path
from .views.test_views import home, hello
from .views.auth_views import register_owner, register_employee, login_user

urlpatterns = [
    path("user/", home, name="user_home"),
    path("test", hello, name="hello"),

    # AUTH URLS
    path("register-owner", register_owner, name="register_owner"),
    path("auth/register-employee/<str:company_code>", register_employee, name="register_employee"),
    path("auth/login", login_user, name="login_user")

    # OTHER URLS
]