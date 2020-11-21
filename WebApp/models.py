from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass

class Admin(models.Model):
    username  = models.CharField(max_length=64)

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=64)
    age = models.IntegerField()
    gender = models.CharField(max_length=64)
    address = models.TextField()
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    date = models.CharField(max_length=64)
    symptoms = models.TextField()
    health_det = models.TextField()
    emg_phone = models.CharField(max_length=64)
    bed = models.CharField(max_length=64)
    venti = models.CharField(max_length=64)
    status = models.CharField(max_length=64)
    condi = models.CharField(max_length=64)
    notes = models.TextField()

class Resource(models.Model):
    beds = models.IntegerField(default=500)
    venti = models.IntegerField(default=200)
    kits = models.IntegerField(default=300)

class Req(models.Model):
    req_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    gender = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    symptoms = models.TextField()
    emg_phone = models.CharField(max_length=64)
