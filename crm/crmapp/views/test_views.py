from django.shortcuts import render 
from ..decorators import role_required
from django.contrib.auth.decorators import login_required
import os

"""
def helo_noob():
  print("this is a test function")
  print(os.getenv("DB_NAME"))
"""

def home(request):
  # helo_noob()
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

