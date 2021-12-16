from django.db import models

# Create your models here.

class Patient(models.Model):
	name = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	bloodtype = models.CharField(max_length=3)
	doctorname = models.CharField(max_length=100)
	lat = models.CharField(max_length=100)
	len = models.CharField(max_length=100)
	def __str__(self):
		return self.name


