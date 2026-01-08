from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('/internetBanking/',views.login_banking,name='internetBanking'),
    path('login/',views.login_banking,name='loginpage'),
    path('register',views.register,name ='register'),
    path('profile/',views.profile,name = 'profile'),
    ]