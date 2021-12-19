from django.db import models
from .useful import *


class Patient(models.Model):
	name = models.CharField(max_length=100,primary_key=True)
	surname = models.CharField(max_length=100)
	hospital_name=models.CharField(max_length=100)
	Doctorname = models.CharField(max_length=100,) #choices will get choices=
	bloodtype = models.CharField(max_length=100)
	email=models.EmailField(max_length = 254)
	lat = models.CharField(max_length=100)
	len = models.CharField(max_length=100)

