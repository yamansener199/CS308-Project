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
from .forms import CreateUserForm ,PatientForm

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
	fields = ['name', 'surname', 'hospital_name', 'Doctorname','bloodtype','lat','len']  # this says to include all fields from model to the form

	for object in u:
		coordinates.append([
			object['name'],
			object['surname'],
			object['hospital_name'],
			object['lat'],
			object['len']])
	for i in range(len(coordinates)):
		lat_len[i]={'patient_name':str(coordinates[i][0]),
					'patient_surname':str(coordinates[i][0]),
					'hospital_name':str(coordinates[i][2]),
					'lat':float(coordinates[i][3]),
					'len':float(coordinates[i][4])}

	dataJSON = dumps(lat_len)
	print(dataJSON)
	return render(request, 'accounts/dashboard.html',{'data': dataJSON})

def submit(request):
	if request.method == 'POST':  # data sent by user
		form = PatientForm(request.POST)
		if form.is_valid():
			form.save()  # this will save Car info to database
			user = form.cleaned_data.get('name')
			messages.info(request, "Your Request Created"+str(user))
			return render(request,'accounts/main.html')
		else:
			print("OPPSSS")
	else:  # display empty form
		form = PatientForm()
	return render(request, 'accounts/submit.html', {'patient_form': form})


@login_required(login_url='login')
def change_data(request):
	return render(request,'accounts/account.html')


		
	