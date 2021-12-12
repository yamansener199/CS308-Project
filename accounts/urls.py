from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	path('whoweare/', views.whoweare, name="whoweare"),
	path('info/', views.info, name="info"),
    path('', views.home, name="home"),

]