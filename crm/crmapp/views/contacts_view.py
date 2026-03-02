from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models.contact import Contact


@csrf_exempt
def get_all_contacts(request):
    return JsonResponse({"error": "This function is still in hold and in progress"})


@csrf_exempt
def create_contact(request):
    pass


@csrf_exempt
def update_contact(request):
    return JsonResponse({"error": "This function is still in hold and in progress"})


@csrf_exempt
def delete_contact(request):
    return JsonResponse({"error": "This function is still in hold and in progress"})


@csrf_exempt
def get_contact_by_id(request):
    return JsonResponse({"error": "This function is still in hold and in progress"})


@csrf_exempt
def reactivate_contact(request):
    return JsonResponse({"error": "This function is still in hold and in progress"})
