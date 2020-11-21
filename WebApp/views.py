from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import User, Admin, Patient, Resource, Req
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.

def index(request):
    r=Resource.objects.order_by('-id')[0]
    beds=r.beds
    venti=r.venti
    pats=Patient.objects.count()
    return render(request, "WebApp/index.html", {"pats": pats, "beds": beds, "venti": venti})


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

def register(request):
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

def add(request):
    if request.method == "POST":
        pat=Patient()
        now=datetime.datetime.now()

        pat.name=request.POST["name"]
        pat.age=request.POST["age"]
        pat.gender=request.POST["gender"]
        pat.address=request.POST["address"]
        pat.phone=request.POST["phone"]
        pat.email=request.POST["email"]
        pat.symptoms=request.POST["symptoms"]
        pat.health_det=request.POST["health_det"]
        pat.bed=request.POST["bed"]
        pat.venti=request.POST["venti"]
        pat.status=request.POST["status"]
        pat.condi=request.POST["condi"]
        pat.emg_phone=request.POST["emg_phone"]
        pat.notes=request.POST["notes"]
        pat.date=now.strftime("%d-%m-%Y")

        pat.save()

        last_res=Resource.objects.order_by('-id')[0]
        if pat.bed=="Yes":
            last_res.beds=int(last_res.beds)-1

        if pat.venti=="Yes":
            last_res.venti=int(last_res.venti)-1

        last_res.kits=int(last_res.kits)-1

        last_res.save()
        
        return render(request, "WebApp/addpatient.html", {"message": "Patient has been added Successfully"})
    
    else:
        return render(request, "WebApp/addpatient.html")

def req(request):
    if request.method == "POST":
        re=Req()

        re.name=request.POST["name"]
        re.age=request.POST["age"]
        re.gender=request.POST["gender"]
        re.address=request.POST["address"]
        re.phone=request.POST["phone"]
        re.email=request.POST["email"]
        re.symptoms=request.POST["symptoms"]
        re.emg_phone=request.POST["emg_phone"]


        re.save()
        
        return render(request, "WebApp/index.html", {"message": "Your request has been recorded."})
    
    else:
        return render(request, "WebApp/request.html")

def dashboard(request):
    if request.method == "POST":
        sp=request.POST["sp"]
        status=request.POST["status"]

        fil=Patient.objects.filter(status=status)
        if sp!="":
            fil=fil.filter(name=sp)

        if fil:
            return render(request, "WebApp/dashboard.html", {"patients": fil})
        else:
            return render(request, "WebApp/dashboard.html", {"patients": None})

    else:
        pat=Patient.objects.all()
        if pat:
            return render(request, "WebApp/dashboard.html", {"patients": pat})
        else:
            return render(request, "WebApp/dashboard.html", {"patients": None})

def reqs(request):
    if request.method == "POST":
        fil=Req.objects.all()
        sp=request.POST["sp"]

        if sp!="":
            fil=fil.filter(name=sp)
            return render(request, "WebApp/allreqs.html", {"requests": fil})
        else:
            return render(request, "WebApp/allreqs.html", {"requests": None})

    else:
        reqs=Req.objects.all()
        if reqs:
            return render(request, "WebApp/allreqs.html", {"requests": reqs})
        else:
            return render(request, "WebApp/allreqs.html", {"requests": None})