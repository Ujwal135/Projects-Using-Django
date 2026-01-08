from django.shortcuts import render, redirect
from .forms import InternetBankingRegisterUser
from accounts.models import Customer_information,Account
from .models import InternetBanking
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from internetBanking.models import InternetBanking

@login_required(login_url='login')
def profile(request):
    # Try to get the customer linked to logged-in user
    try:
        internet_banking = request.user.internetbanking
        customer = internet_banking.customer
        accounts = customer.accounts.all()  # get all accounts
    except InternetBanking.DoesNotExist:
        # If user has no internet banking account, redirect to login
        return redirect('login')

    return render(request, 'internetBanking/profile.html', {
        'customer': customer,
        'accounts': accounts
    })



def loginpage(request):
    
    return render(request, 'internetBanking/homeloginpage.html')

def homeloginpage(requets):
    
    return render(requets,'internetBanking/homeloginpage.html')


def register(request):
    form = InternetBankingRegisterUser(request.POST)
    if request.method == 'POST':
        
        print(request)
        if form.is_valid():
            customer_id = form.cleaned_data['customer_id']
            account_number = form.cleaned_data['account_number']
            mobile_number = form.cleaned_data['mobile_number']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            

            
            
            try:
                customer = Customer_information.objects.get(
                    customer_id=customer_id,
                    mobile=mobile_number
                )
                account = Account.objects.get(
                    customer = customer,
                    account_number = account_number
                )

                if InternetBanking.objects.filter(customer=customer).exists():
                    messages.error(request, "Internet banking is already activated")
                    return redirect("loginpage")

                if User.objects.filter(username=username).exists():
                    messages.error(request, "Please select a different username")
                    return redirect("loginpage",)

                with transaction.atomic():
                    user = User.objects.create_user(
                        username=username,
                        password=password
                    )
                    print("User created:", user.username)

                    InternetBanking.objects.create(
                        user=user,
                        customer=customer
                    )

                messages.success(request, "Registration successful. Please login")
                return redirect("loginpage")

            except Customer_information.DoesNotExist:
                print(messages.error(request, "Invalid customer details"))
                messages.error(request, "Invalid customer details")
        else:
            print("form error",form.errors)
    else:
        messages.error(request,form.errors)

    return render(request, 'internetBanking/register.html', {'form': form})


def login_banking(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user =  authenticate(request,username = username,password = password)
        
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request,"Invalid username or password")
    
    return render(request,'internetBanking/homeloginpage.html')


@login_required(login_url='login')
def profile(request):
    
    try:
        internetBanking = request.user.internetbanking
        customer = internetBanking.customer
        accounts = customer.accounts.all()
    
    except Exception as e:
        print(e)
        return redirect('loginpage')
    
    return render(request,'internetBanking/profile.html' ,{
        'customer': customer,
        'accounts': accounts
    })