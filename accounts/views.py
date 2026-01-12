from django.shortcuts import render,redirect
from .forms import Customer_Form
from .models import Customer_information,Account
import uuid
from datetime import date
from.utils import render_to_pdf
from django.http import HttpResponse

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
        internet_banking_activate = request.POST.get('internet_banking_activate')
        account = Account.objects.create(
            customer = customer,
            account_type=account_type,
            internet_banking_is_active = internet_banking_activate,
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
    
    
def passbook_pdf(request,account_id):
    account = Account.objects.get(id=account_id)
    customer = account.customer
   
    params = {
       'account':account,
       'customer':customer
   }
    
    pdf = render_to_pdf('accounts/passbook.html',params)
    print(type(pdf)) 
    
    if pdf is None:
        return HttpResponse("PDF generation failed", status=500)
    
    return HttpResponse(pdf, content_type='application/pdf')