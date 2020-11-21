from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("add", views.add, name="add"),
    path("request", views.req, name="request"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("requests", views.reqs, name="reqs"),
    path("patient/<id>", views.indipatient, name="indipatient"),
    path("update/<id>", views.update, name="update"),
    path("request/<id>", views.indirequest, name="indirequest")
]