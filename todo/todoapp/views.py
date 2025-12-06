# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from todoapp import models
from todoapp.models import Todo
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required



 
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
    if request.method == "POST":
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        print(fnm,pwd)
        userr = authenticate(request,username=fnm,password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/todos')
        else:
            return redirect('/signin')

    return render(request,'todoapp/login.html') 


def todos(request):
    if request.method =='POST':
        title = request.POST.get('title')
        obj = models.Todo(title = title,user = request.user)
        obj.save()
        return redirect('/todos')
    
    res = models.Todo.objects.filter(user = request.user).order_by('-date')
    return render(request, 'todoapp/todopage.html',{'res':res})

def delete_todo(request,srno):
    print(srno)
    obj = models.Todo.objects.get(srno = srno)
    obj.delete()
    return redirect('/todos')



@login_required(login_url='/login')

def edit_todo(request, srno):
    
    obj = get_object_or_404(models.Todo, srno=srno, user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.Todo.objects.get(srno=srno)
        obj.title = title
        obj.save()
        return redirect('todopage')

    # obj = models.Todo.objects.get(srno=srno)
    res = models.Todo.objects.filter(user=request.user)
    
    return render(request, 'edit_todo.html', {'obj': obj,'res':res})





def signout(request):
    logout(request)
    return redirect('/login')