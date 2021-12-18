from django.contrib import admin
from django.contrib.auth.models import User
from accounts.forms import Patient

# Register your models here.
from .models import *
admin.site.register(Patient)
