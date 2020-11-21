from django.contrib import admin
from .models import User, Patient, Admin, Resource, Req

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Patient)
admin.site.register(Resource)
admin.site.register(Req)