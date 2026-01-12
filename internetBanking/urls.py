from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('/internetBanking/',views.login_banking,name='internetBanking'),
    path('login/',views.login_banking,name='loginpage'),
    path('logout/',views.logout_banking,name = 'logout_banking'),
    path('register',views.register,name ='register'),
    path('profile/',views.profile,name = 'profile'),
    path('banktobanktransfer/',views.banktobanktransfer,name = "bank_transfer"),
    path("credit/", views.credit_and_debit, name="credit_amount"),
    path("debit/", views.credit_and_debit, name="credit_amount"),
    path("transactions/", views.transaction_list, name="transactions"),
    path("balance/", views.account_dets, name="account_balance"),
    path("statement/", views.bank_statement, name="bank_statement"),
    ]