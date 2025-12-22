from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('saving_account/', views.saving_account_home, name='saving_account'),
]