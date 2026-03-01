from django.contrib import admin
from django.urls import include, path
from .views.user_views import home
from .views.auth_views import register_owner,login_user
from .views.deals_views import create_deal,deal_list,test_page

urlpatterns = [
    path("user/", home, name="user_home"),
    path("register-owner/", register_owner, name="register_owner"),
    path("create-deals/",create_deal, name="create_deal"),
    path("deal-list/",deal_list, name="deal_list"),
    path("", test_page, name="test_page"),
] 