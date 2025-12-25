from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('open-account/', views.openform, name='open_account_form'),
    path('saving-account/<int:customer_id>/', views.saving_account, name='saving_account'),
]
