from django.shortcuts import render, redirect
from .forms import InternetBankingRegisterUser,Banktobanktransfer,Creditamountform
from accounts.models import Customer_information,Account
from .models import InternetBanking
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from internetBanking.models import InternetBanking,Ibtransactions
from django.views.decorators.csrf import csrf_exempt
import qrcode as qrcode
from decimal import Decimal 





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
                    account_number = account_number,
                )

                if InternetBanking.objects.filter(customer=customer).exists():
                    messages.error(request, "Internet banking is already activated")
                    return redirect("loginpage")
                
                if Account.objects.filter(customer = customer ,internet_banking_is_active = "N").exists():
                    messages.error(request,"Internet banking is not activated ,Contact Admin ")
                    return redirect("register.html")

                if User.objects.filter(username=username).exists():
                    messages.error(request, "Please select a different username")
                    return redirect("loginpage",)

                with transaction.atomic():
                    user = User.objects.create_user(
                        username=username,
                        password=password
                    )
                    customer.user = user
                    customer.save()
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
    
    services = [
        {
            "title": "Bank to Bank Transfer",
            "desc": "Transfer money securely to other banks",
            "icon": "🔁",
            "name": "bank_transfer"
        },
        {
            "title": "Credit Amount",
            "desc": "Deposit money into your account",
            "icon": "➕",
            "name": "credit_amount"
        },
        {
            "title": "Debit Amount",
            "desc": "Withdraw money from your account",
            "icon": "➖",
            "name": "credit_amount"
        },
        {
            "title": "Transaction History",
            "desc": "View all your transactions",
            "icon": "📜",
            "name": "transactions"
        },
        {
            "title": "Account Balance",
            "desc": "Check available balance",
            "icon": "💰",
            "name": "account_balance"
        },
        {
            "title": "Download Statement",
            "desc": "Download bank statement (PDF)",
            "icon": "📄",
            "name": "bank_statement"
        },
    ]

    # animation delay
    for i, service in enumerate(services):
        service["delay"] = round(i * 0.15, 2)

    
    return render(request,'internetBanking/profile.html' ,{
        'customer': customer,
        'accounts': accounts,
        'services':services
    })
    
def logout_banking(request):
        logout(request)
        return redirect('loginpage')
    
@login_required(login_url='login')
def credit_and_debit(request):
    
    form = Creditamountform(request.POST)
    if request.method == "POST":
        
        if form.is_valid():
        
        
            internet_banking = InternetBanking.objects.get(user = request.user)
            customer = internet_banking.customer
            amount = form.cleaned_data["amount"]
            amount = Decimal(amount)
            self_account = Account.objects.filter(customer = customer).first()
            
            # QR GEN
            data = f"user_id={customer.id}& type=credit"
            
            qr = qrcode.make(data)
            qr_path = f'media/{customer.id}.png'
            qr.save(qr_path)
            
             
            with transaction.atomic():
                self_account.balance += amount
                self_account.save()

            # Sender transaction
            Ibtransactions.objects.create(
                user=request.user,
                transaction_type='CR',
                receiver_account="self_online ",
                sender_account="self_online",
                amount=amount,
                balance_after=self_account.balance,
                remark="Credited")
            
            messages.success(request, "Amount credited successfully")
            return redirect("profile")

    return render(request, "internetBanking/credit_and_debit.html",{"qr_path":qr_path})

from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib import messages


@login_required(login_url='login')
def banktobanktransfer(request):

    form = Banktobanktransfer(request.POST or None)

    if request.method == "POST" and form.is_valid():

        # 1️⃣ Get customer linked to logged-in user via InternetBanking
        try:
            internet_banking = InternetBanking.objects.get(user=request.user)
            print(internet_banking)
            customer = internet_banking.customer
            print(customer)
        except InternetBanking.DoesNotExist:
            messages.error(request, "Internet banking not activated")
            return redirect("loginpage")

        # 2️⃣ Get sender account (assuming single account per customer)
        sender_account = Account.objects.filter(customer=customer).first()
        print(sender_account)
        if not sender_account:
            messages.error(request, "No bank account found")
            return redirect("loginpage")

        receiver_account_no = form.cleaned_data['account_number']
        confirm_account = form.cleaned_data['confirm_account']
        amount = form.cleaned_data['amount']

        # 3️⃣ Account number mismatch
        if receiver_account_no != confirm_account:
            messages.error(request, "Account number does not match")
            return render(request, 'internetBanking/btobtrf.html', {'form': form})

        # 4️⃣ Get receiver account
        try:
            receiver_account = Account.objects.get(account_number=receiver_account_no)
        except Account.DoesNotExist:
            messages.error(request, "Receiver account not found")
            return render(request, 'internetBanking/btobtrf.html', {'form': form})

        # 5️⃣ Insufficient balance
        if sender_account.balance < amount:
            messages.error(request, "Insufficient balance")

            Ibtransactions.objects.create(
                user=request.user,
                transaction_type='DBT',
                receiver_account=receiver_account_no,
                sender_account=sender_account.account_number,
                amount=amount,
                balance_after=sender_account.balance,
                remark="Insufficient balance"
            )
            return render(request, 'internetBanking/btobtrf.html', {'form': form})

        # 6️⃣ SUCCESS TRANSFER (ATOMIC)
        with transaction.atomic():
            sender_account.balance -= amount
            sender_account.save()

            receiver_account.balance += amount
            receiver_account.save()

            # Sender transaction
            Ibtransactions.objects.create(
                user=request.user,
                transaction_type='DBT',
                receiver_account=receiver_account.account_number,
                sender_account=sender_account.account_number,
                amount=amount,
                balance_after=sender_account.balance,
                remark="Transfer success"
            )

            # Receiver transaction
            if receiver_account.customer.user:
                Ibtransactions.objects.create(
                    user=receiver_account.customer.user,
                    transaction_type='CR',
                    receiver_account=receiver_account.account_number,
                    sender_account=sender_account.account_number,
                    amount=amount,
                    balance_after=receiver_account.balance,
                    remark="Amount received"
                )

        messages.success(request, "Transfer completed successfully")
        return redirect('profile')

    return render(request, 'internetBanking/btobtrf.html', {'form': form})



    

def transaction_list(request):  
    
    return render(request,"internetBanking/last10trans.html")

def account_dets(request):
    return render(request,"internetBanking/profile.html")

def bank_statement(request):
    return render(request,"internetBanking/statemen.html")