from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models.contact import Contact


@csrf_exempt
def get_all_leads(request):
  return JsonResponse({
    "error": "This function is still in hold and in progress"
  })

@csrf_exempt
def create_lead(request):
  return JsonResponse({
    "error": "This function is still in hold and in progress"
  })

@csrf_exempt
def update_lead(request):
  return JsonResponse({
    "error": "This function is still in hold and in progress"
  })

@csrf_exempt
def delete_lead(request):
  return JsonResponse({
    "error": "This function is still in hold and in progress"
  })

@csrf_exempt
def get_lead_by_id(request):
  return JsonResponse({
    "error": "This function is still in hold and in progress"
  })

@csrf_exempt
def reactivate_lead(request):
  return JsonResponse({
    "error": "This function is still in hold and in progress"
  })