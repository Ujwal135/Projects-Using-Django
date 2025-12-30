from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('open-account-form/', views.openform, name='open_account_form'),
    path('open-account/',views.openform,name='open_account'),
    path('saving-account/<int:customer_id>/', views.saving_account, name='saving_account'),
    path('create-account/<int:customer_id>/', views.create_account, name='create_account'),
    path('account-success/<int:account_id>/',views.account_success,name='account_success'),
    path('account/passbook/<int:account_id>/',views.passbook_pdf, name='passbook_pdf'),

    
    
]
