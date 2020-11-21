from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import User, Admin, Patient, Resource
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.

def index(request):
    return render(request, "WebApp/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        i_id=username
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return render(request, "WebApp/index.html", {"i_id": username, "message": f"Logged In as: {i_id}"})
        else:
            return render(request, "WebApp/login.html", {"message": "Invalid username and/or password."})
    else:
        return render(request, "WebApp/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register_admin(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        code = request.POST["code"]

        if code!="9238912":
            return render(request, "WebApp/register.html", {"message": "Incorrect Authentication Code."})
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "WebApp/register.html", {"message": "Passwords must match."})

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "WebApp/register.html", {"message": "Username Taken"})
        login(request, user)
        return render(request, "WebApp/index.html", {"i_id": username, "message": "Account Created Successfully"})
    else:
        return render(request, "WebApp/register.html")

def register_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "WebApp/register.html", {"message": "Passwords must match."})

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "WebApp/register.html", {"message": "Username Taken"})
        login(request, user)
        return render(request, "WebApp/index.html", {"i_id": username, "message": "Account Created Successfully"})
    else:
        return render(request, "WebApp/register.html")

def add(request):
    if request.method == "POST":
        return HttpResponse("Hello")
    
    else:
        return render(request, "WebApp/addpatient.html")