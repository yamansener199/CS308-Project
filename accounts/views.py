from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm

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
	return render(request, 'accounts/dashboard.html')

def submit(request):
	if request.method == 'POST':
		name=request.POST.get('name')
		surname=request.POST.get('surname')
		bloodtype=request.POST.get('bloodtype')
		doctorname=request.POST.get('doctor_name')
		lat=request.POST.get('Lat')
		len=request.POST.get('Len')
		patient = Patient.objects.create(name=name,
										surname=surname,
										bloodtype=bloodtype,
										doctorname=doctorname,
										lat=lat,
										len=len	
													)
		messages.success(request, 'Request created for : ' +str(name))
		render(request,'accounts/main.html')
	return render(request, 'accounts/submit.html')

@login_required(login_url='login')
def change_data(request):
	return render(request,'accounts/account.html')


		
	