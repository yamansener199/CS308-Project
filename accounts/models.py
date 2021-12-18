from django.db import models

# Create your models here.

class Patient(models.Model):
	name = models.CharField(max_length=100,primary_key=True)
	surname = models.CharField(max_length=100)
	hospital_name=models.CharField(max_length=100)
	Doctorname = models.CharField(max_length=100)
	bloodtype = models.CharField(max_length=100)
	lat = models.CharField(max_length=100)
	len = models.CharField(max_length=100)
	