from django.contrib import admin
from django.urls import include, path
from .views.test_views import home, hello
from .views.auth_views import register_owner, register_employee, login_user, get_current_user, logout_user, delete_user, reactivate_user, change_roles, change_password
from .views.company_views import get_all_users

urlpatterns = [
    path("user/", home, name="user_home"),
    path("test", hello, name="hello"),

    # AUTH URLS
    path("register-owner", register_owner, name="register_owner"),
    path("auth/register-employee/<str:company_code>", register_employee, name="register_employee"),
    path("auth/login", login_user, name="login_user"),
    path("auth/me", get_current_user, name="get_current_user"),
    path("auth/logout", logout_user, name="logout_user"),
    path("auth/<str:user_id>/delete", delete_user, name="delete_user"),
    path("auth/<str:user_id>/reactivate", reactivate_user, name="reactivate_user"),
    path("auth/<str:user_id>/change-role", change_roles, name="change_roles"),
    path("auth/<str:user_id>/change-pass", change_password, name="change-pass"),

    # COMPANY URLS
    path("comp/<str:company_id>/users", get_all_users ,name="get_all_users")


    # OTHER URLS
]   