from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	path('whoweare/', views.whoweare, name="whoweare"),
	path('info/', views.info, name="info"),
	path('hospital_displays/', views.hospital_displays, name="hospital_displays"),
	path('how_to_help/',views.help,name="help"),
	path('submit/', views.submit, name="submit"),
	path('doctor_profile/', views.doctor_profile, name="doctor_profile"),
	path('hospitalinfo/', views.CantfindHospital, name="hospitalinfo"),
    path('', views.home, name="home"),
]