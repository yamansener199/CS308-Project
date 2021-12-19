from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from json import dumps
from .models import *
import json
from .forms import CreateUserForm ,PatientForm
from .useful import ReadData
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('login')
			
		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)
		
@login_required
def logoutUser(request):
	logout(request)
	return redirect('home')

def whoweare(request):
	return render(request, 'accounts/whoweare.html')

def info(request):
	return render(request, 'accounts/info.html')

def home(request):
	coordinates=[]
	lat_len={}
	u = Patient.objects.values()
	#fields = ['name', 'surname', 'hospital_name', 'Doctorname','bloodtype','lat','len']  # this says to include all fields from model to the form
	for object in u:
		coordinates.append([
			object['name'],
			object['surname'],
			object['hospital_name'],
			object['lat'],
			object['len'],
			object['Doctorname'],
			object['bloodtype']])
	for i in range(len(coordinates)):
		lat_len[i]={'patient_name':str(coordinates[i][0]),
					'patient_surname':str(coordinates[i][1]),
					'hospital_name':str(coordinates[i][2]),
					'lat':float(coordinates[i][3]),
					'len':float(coordinates[i][4]),
					'Doctorname':str(coordinates[i][5]),
					'bloodtype':str(coordinates[i][6])}
	dataJSON = dumps(lat_len)
	return render(request, 'accounts/dashboard.html',{'data': dataJSON})

def submit(request):
	if request.method == 'POST': 
		form = PatientForm(request.POST)
		if form.is_valid():
			form.save()  
			username = form.cleaned_data.get('name')
			usersurname = form.cleaned_data.get('name')
			messages.info(request, "Your Request Created"+str(username)+" "+str(usersurname))
			return render(request,'accounts/main.html',)
		else:
			print("GO BACK HACI !")
	else: 
		form = PatientForm()
	return render(request, 'accounts/submit.html', {'patient_form': form,'objectlist': User.objects.only('username')})

def CantfindHospital(request):
	df=ReadData()
	{'DataFrame': df }
	return render(request, 'accounts/hospitalinfo.html',{'DataFrame': df })

def help(request):
	return render(request, 'accounts/help.html')

@login_required(login_url='login')
def doctor_profile(request):
	user_profile=Patient.objects.filter(Doctorname=request.user.username)
	print(user_profile)
	return render(request,'accounts/doctor_profile.html',{'user_profile': user_profile})


		
	