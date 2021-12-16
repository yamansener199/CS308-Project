from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Patient

CHOICES =(
    ("1", "A positive"),
    ("2", "B positive"),
    ("3", "A negative"),
    ("4", "B negative"),
    ("5", "AB negative"),
	("6", "AB positive")
)
#Can create choices in build here about the doctors for choosing the doctor


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class PatientForm(forms.Form):
	name = forms.CharField(label='Your name' ,max_length=100)
	surname = forms.CharField(label='Your name' ,max_length=100)
	bloodtype = forms.ChoiceField(choices = CHOICES)
	email=forms.EmailField(label='Email',max_length=100)
	doctorname = forms.CharField(label='Your name' ,max_length=100)
	lat = forms.CharField(label='Your name' ,max_length=100)
	len = forms.CharField(label='Your name' ,max_length=100)
	class Meta:
		model = Patient
		fields = ('name', 'surname', 'bloodtype','doctorname','lat','len')
