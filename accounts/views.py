from django.shortcuts import render,redirect
from .forms import Customer_Form
from .models import Customer_information

# Create your views here.

def openform(request):
    customer = None
    show_popup = False
    form = Customer_Form()
    
    
    if request.method == 'POST':
        form = Customer_Form(request.POST)
        if form.is_valid():
            customer = form.save()
            show_popup = True
            return redirect('saving_account',customer_id = customer.customer_id)
            
        
    return render(request, 'accounts/open_account.html', {
        'form': form})
    
def saving_account(request, customer_id):
    customer = Customer_information.objects.get(id=customer_id)

    return render(request, 'accounts/saving_account.html', {
        'customer': customer
    })

def opensavingaccount(request,customer_id):
    return render(request,'accounts/saving_account.html')