from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from ..models.common import Company
from ..models.user import Userprofile

"""
-> GET ALL USERS FLOW
    req method check
    get company through code

"""

@csrf_exempt
def get_all_users(request, company_id):
  if request.method != "GET":
    return JsonResponse({"error": "GET request required"}, status=405)

  company = Company.objects.get(code=company_id)
  if not company:
    return JsonResponse({"error": "Company does not exists"}, status=404)
  
  return JsonResponse({
    "message": "Fetched company from company id", 
    "company": company.title,
    "domain": company.domain,
  })