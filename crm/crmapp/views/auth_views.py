import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from ..models.common import Company
from ..models.user import Userprofile


"""
  THINGS TO DO
  1. NEED TO SHIFT TO CBV(CLASS BASED VIEWS) AFTER CREATING MORE API FUNCTIONS/CONTROLLERS
  2. USE JWT OR SESSION API FOR AUTH SYSTEMS
  3. ADD ROLE BASED ACCESS
  4. CREATING, INVITE LINKS AND INVITE MODEL 
  5. REGISTERING MEMBERS BASED ON INVITE LINKS
"""


@csrf_exempt    # FOR TEMPORARY BASIC(DEV) CAN USE PROPER CSRF/AUTH
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
    first_name = data.get("first_name")
    last_name = data.get("last_name")

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
        password=password,
        first_name = first_name,
        last_name = last_name
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
  

@csrf_exempt   # DEV ONLY NEED CHANGE
def register_employee(request, company_code):
  if request.method != "POST":
    return JsonResponse({"error": "POST request required"}, status=400)
  
  try:
    data = json.loads(request.body)

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    first_name = data.get("first_name")
    last_name = data.get("last_name")

    company = get_object_or_404(Company, code=company_code)

    if User.objects.filter(username=username).exists():
      return JsonResponse({"error": "Username already exists"}, status=400)

    if User.objects.filter(email=email).exists():
      return JsonResponse({"error": "Email already exists"}, status=400)

    if not company:
      return JsonResponse({"error": "Unauthorized request, invalid company code"}, status=401)

    with transaction.atomic():

      user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
      )

      profile, created = Userprofile.objects.get_or_create(user=user)
      profile.role = "member"
      profile.company = company
      profile.save()

    return JsonResponse(
      {
        "message": "Created employee user",
        "company": company.title,
        "role": "member"
      },
      status=201
    )
  except Exception as e:
    return JsonResponse({"error": str(e)}, status=400)
  

@csrf_exempt   # DEV ONLY NEED CHANGE
def login_user(request):
  if request.method != "POST":
    return JsonResponse({"error": "POST request required"}, status=400)

  data = json.loads(request.body)
  username = data.get("username")
  password = data.get("password")

  user = authenticate(request, username=username, password=password)

  if user is not None:
    login(request, user)
    profile, created = Userprofile.objects.get_or_create(user=user)
    return JsonResponse({
      "message": "Login successfull",
      "username": user.username,
      "role": profile.role,
      "company": profile.company.title
    }, status=200)
  else:
    return JsonResponse({"error": "Invalid username or password"}, status=401)

@csrf_exempt
def get_current_user(request):
  if request.method != "GET":
    return JsonResponse({"error": "GET request required"}, status=400)

  # GET CURRENT USER LOGIC SHOULD BE HERE