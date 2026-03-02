from django.contrib import admin
from django.urls import include, path
from .views.test_views import home, hello
from .views.auth_views import (
    register_owner,
    register_employee,
    login_user,
    get_current_user,
    logout_user,
    delete_user,
    reactivate_user,
    change_roles,
    change_password,
)
from .views.company_views import (
    get_all_users,
    get_company,
    update_company,
    delete_company,
    reactivate_company,
)
from .views.contacts_view import (
    create_contact,
    get_all_contacts,
    get_contact_by_id,
    update_contact,
    delete_contact,
    reactivate_contact,
)
from .views.lead_view import (
    create_lead,
    get_all_leads,
    get_lead_by_id,
    update_lead,
    delete_lead,
    reactivate_lead,
)
from .views.task_view import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task,
    reactivate_task,
)

urlpatterns = [
    # TESTING URLS (TEMPORARY)
    path("user/", home, name="user_home"),
    path("test", hello, name="hello"),

    # AUTH URLS
    path("auth/register-owner", register_owner, name="register_owner"),
    path(
        "auth/register-employee/<str:company_code>",
        register_employee,
        name="register_employee",
    ),
    path("auth/login", login_user, name="login_user"),
    path("auth/me", get_current_user, name="get_current_user"),
    path("auth/logout", logout_user, name="logout_user"),
    path("auth/<str:user_id>/delete", delete_user, name="delete_user"),
    path("auth/<str:user_id>/reactivate", reactivate_user, name="reactivate_user"),
    path("auth/<str:user_id>/change-role", change_roles, name="change_roles"),
    path("auth/change-password", change_password, name="change-pass"),
    
    # COMPANY URLS
    path("comp/users", get_all_users, name="get_all_users"),
    path("comp/get-company", get_company, name="get_company"),
    path("comp/delete", delete_company, name="delete_company"),
    path("comp/delete", delete_company, name="delete_company"),
    path("comp/reactivate", reactivate_company, name="reactivate_company"),  # TEMP

    # CONTACT URLS
    path("comp/contact/all", get_all_contacts, name="get_all_contacts"),
    path("comp/contact/get", get_contact_by_id, name="get_contact_by_id"),
    path("comp/contact/create", create_contact, name="create_contact"),
    path("comp/contact/update", update_contact, name="update_contact"),
    path("comp/contact/delete", delete_contact, name="delete_contact"),
    path(
        "comp/contact/reactivate", reactivate_contact, name="reactivate_contact"
    ),  # TEMP

    # LEAD URLS
    path("comp/lead/all", get_all_leads, name="get_all_leads"),
    path("comp/lead/get", get_lead_by_id, name="get_lead_by_id"),
    path("comp/lead/create", create_lead, name="create_lead"),
    path("comp/lead/update", update_lead, name="update_lead"),
    path("comp/lead/delete", delete_lead, name="delete_lead"),
    path("comp/lead/reactivate", reactivate_lead, name="reactivate_lead"),

    # DEAL URLS


    # TASK URLS
    path("comp/task/all", get_all_tasks, name="get_all_tasks"),
    path("comp/task/get", get_task_by_id, name="get_task_by_id"),
    path("comp/task/create", create_task, name="create_task"),
    path("comp/task/update", update_task, name="update_task"),
    path("comp/task/delete", delete_task, name="delete_task"),
    
    # OTHER URLS

]
