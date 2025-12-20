from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('home/',views.home,name = 'home'),
    path('account/',views.account,name='account'),
    path('loan/',views.loan,name='loan'),
    path('cards/',views.cards,name='cards'),
    path('insurance/',views.insurance,name='insurance'),
    path('support/',views.support,name='support'),
    path('investments/',views.investments,name='investments')
]

