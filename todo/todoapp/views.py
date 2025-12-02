# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from todoapp import models
from todoapp.models import Todo



 
def signup(request):
    
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('pwd')
        print(fnm,emailid,pwd)
        
        my_user = User.objects.create_user(fnm,emailid,pwd)
        my_user.save()
        
        return redirect('/login')
        
    return render (request ,'todoapp/signin.html')

def loginn(request):
    return render(request,'todoapp/login.html')