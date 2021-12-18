from django.db import models
from .useful import *

class Patient(models.Model):
	name = models.CharField(max_length=100,primary_key=True)
	surname = models.CharField(max_length=100)
	hospital_name=models.CharField(max_length=100)
	Doctorname = models.CharField(max_length=100,) #choices will get choices=
	bloodtype = models.CharField(max_length=100)
	lat = models.CharField(max_length=100)
	len = models.CharField(max_length=100)

class Data(models.Model):
  il = models.IntegerField(primary_key=True)
  ilce=models.CharField(max_length=200)
  name=models.CharField(max_length=200)
  category=models.CharField(max_length=200)
  building=models.CharField(max_length=200)
  img_count=models.CharField(max_length=200)
  lat = models.CharField(max_length=100)
  len = models.CharField(max_length=100)

