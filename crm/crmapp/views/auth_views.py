import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.contrib.auth.models import User
from ..models.common import Company
from ..models.user import Userprofile

@csrf_exempt
def register_owner(request):
  if request.method != "POST":
    return JsonResponse({"error": "POST method required"}, status=400)
  
  try:
    data = json.loads(request.body)
    
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    company_name = data.get("company_name")
    domain = data.get("domain")
    phone = data.get("phone")
    country = data.get("country")
    address = data.get("address")

    with transaction.atomic():

      company = Company.objects.create(
        title = company_name,
        domain = domain,
        phone = phone,
        country = country,
        address = address
      )

      user  = User.objects.create_user(
        username=username,
        email=email,
        password=password
      )

      Userprofile.objects.create(
        user=user,
        company=company,
        role="admin"
      )
    
    return JsonResponse({
      "message": "Company and owner created successfully",
      "company_code": company.code
    }, status=201)
  
  except Exception as e:
    return JsonResponse({"error": str(e)}, status=400)
  

@csrf_exempt
def register_users(request):
  pass
  # ON-HOLD WILL BE COMPLETED LATER