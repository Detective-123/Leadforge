from django.shortcuts import render
from ..decorators import role_required
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import os

'''
SAMPLE VERIFICATION EMAIL

def helo_noob(request):

    subject = "Verify your CRM Account"

    message = "Please verify your account."  # fallback plain text

    html_message = f"""
    <div style="font-family: Arial, sans-serif;">
        <h2>Welcome to Your CRM 🚀</h2>
        <p>Click the button below to verify your account:</p>
        
        <a href="http://127.0.0.1:8000/api/test" 
           style="
           display: inline-block;
           padding: 10px 20px;
           font-size: 16px;
           color: white;
           background-color: #4CAF50;
           text-decoration: none;
           border-radius: 5px;">
           Verify Email
        </a>

        <p>If you didn’t create this account, ignore this email.</p>
    </div>
    """

    send_mail(
        subject=subject,
        message=message,
        from_email="leadforgecrm@mail.com",
        recipient_list=["example@mail.com"],
        html_message=html_message,
    )
'''

def home(request):
  # helo_noob(request)
  return render(request, "home.html")


@login_required
def hello(request):
  print("THIS IS AN IMPORTANT PRINT", request.user)
  print(request.user.is_authenticated)
  return render(request, "denied.html")


"""
-----LOGIN WITH TEMPLATE RENDERING------

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/api/test")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")
"""
