from django.shortcuts import render,redirect
from .forms import Customer_Form
from .models import Customer_information,Account
import uuid
from datetime import date

# Create your views here.

def openform(request):
    form = Customer_Form()

    if request.method == 'POST':
        form = Customer_Form(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('saving_account', customer_id = customer.id)

    return render(request, 'accounts/open_account.html', {
        'form': form
    })
    
def saving_account(request,customer_id):
    
    customer = Customer_information.objects.get(id = customer_id)
    
    if request.method == 'POST':
        print("CONFIRM BUTTON CLICKED")
        return redirect('create_account', customer_id=customer.id)

    return render(request, 'accounts/saving_account.html', {
        'customer': customer })


def create_account(request,customer_id):
    
    customer = Customer_information.objects.get(id = customer_id)
    
    if request.method == 'POST':
        account_type = request.POST.get('account_type')
        
        account = Account.objects.create(
            customer = customer,
            account_type=account_type,
            # account_number = generate_account_number(account_type)
            balance = 0
        )
        
        return redirect('account_success',account_id = account.id)
    return render(request,'accounts/create_account.html',{"customer":customer})


def account_success(request,account_id):
    account = Account.objects.get(id=account_id)
    customer = account.customer

    return render(request, 'accounts/success.html', {
        'account': account,
        'customer': customer
    })
    

# def generate_account_number(account_type):
#     prefix = 'SAV' if account_type == 'SAV' else 'CUR'
#     keyword = 'SUPR' 
#     unique = str(uuid.uuid4().int)[-6:]

#     return f'{prefix}-{keyword}-{unique}'
