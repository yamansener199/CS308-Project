from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Patient

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class PatientForm(ModelForm):
	lat = forms.CharField(
    label = 'latitude',
    max_length = 2000,
    required = True,
    widget = forms.TextInput(
        attrs = {'id': 'latt', 'name': 'lat',}
        )
    )
	len = forms.CharField(
    label = 'len',
    max_length = 2000,
    required = True,
    widget = forms.TextInput(
        attrs = {'id': 'lenn', 'name': 'len'}
        )
    )
	class Meta:
		model = Patient
		fields = ['name', 'surname', 'hospital_name', 'Doctorname','bloodtype','email','lat','len']  # this says to include all fields from model to the form
