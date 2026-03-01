import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.contrib.auth.models import User
from ..models.common import Company
from ..models.user import Userprofile
from django.shortcuts import render ,redirect
from .auth_views import login_user
from ..models.deal import Deal
from ..models.contact import Contact
from django.contrib.auth.decorators import login_required

@login_required
def create_deal(request,contact_id):
    if request.method!="POST":
        return JsonResponse({"error":"post request required"},status=405)
    
    if not request.user.is_authenticated :
        return JsonResponse({"error":"not authenticated user"},status=401)
    
    data=json.loads(request.body)
    value=data.get('value')
    stage=data.get('stage')
    expected_closed_date=data.get('closedate')
    note=data.get('note')
    profile=request.user.userprofile
    company=profile.company
    owner=request.user
    #hello
    
    try:
        contact = Contact.objects.get(id=contact_id)
    except Contact.DoesNotExist:
        return JsonResponse({"error": "Invalid contact"}, status=400)
        
    with transaction.atomic():
        Deal.objects.create(
            owner=owner,
            company=company,
            contact=contact,
            value=value,
            stage=stage,
            expected_closed_date=expected_closed_date,
            note=note 
        )
        
    return JsonResponse(
            {"message": "Deal created successfully"},
            status=201
        )
    
def deal_list(request):

    if request.method != "GET":
        return JsonResponse(
            {"error": "GET request required"},
            status=400
        )

    deals = Deal.objects.filter(
        owner=request.user
    ).select_related("company", "contact")

    deal_data = []

    for deal in deals:
        deal_data.append({
            "id": deal.id,
            "company_id": deal.company,
            "company_name": deal.company,
            "contact_id": deal.contact,
            # "contact_name": deal.contact.name,  # change if different field ok beta samja kyaaaaaa
            "value": str(deal.value),
            "stage": deal.stage,
            "expected_closed_date": str(deal.expected_closed_date),
            "note": deal.note,
            "created_at": str(deal.created_at),
        })

    return JsonResponse(
        {"deals": deal_data},
        status=200
    )
def test_page(request):
    return render(request,"deals.html")