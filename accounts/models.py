from django.db import models

# Create your models here.

class Patient(models.Model):
	name = models.CharField(max_length=100,default="")
	surname = models.CharField(max_length=100,default="")
	bloodtype = models.CharField(max_length=3,default="")
	doctorname = models.CharField(max_length=100,default="")
	lat = models.CharField(max_length=100,default="")
	len = models.CharField(max_length=100,default="")
	def __str__(self):
		return self.name


