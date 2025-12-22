from django.shortcuts import render

# Create your views here.

def saving_account_home(request):
    
    return render(request ,'accounts/savingaccount.html')