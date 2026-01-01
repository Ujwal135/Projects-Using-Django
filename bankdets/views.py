from django.shortcuts import render

# Create your views here.

    
def home(request):
    services = [
        {"title": "Accounts", "desc": "Open your Saving account at 0 balance", "icon": "💰","name":'account'},
        {"title": "Internet-Banking", "desc": "Quick money transfer and many more services", "icon": "🏦","name":'internetBanking'},
        {"title": "Cards", "desc": "Debit and credit cards", "icon": "💳","name":'cards'},
        {"title": "Insurance", "desc": "Life & health coverage", "icon": "🛡️","name":'insurance'},
        {"title": "Investments", "desc": "Grow your wealth", "icon": "📈","name":'investments'},
        {"title": "Support", "desc": "24×7 customer support", "icon": "☎️","name":'support'},
    ]

    # Add staggered animation delay
    for i, service in enumerate(services):
        service['delay'] = round(i * 0.15, 2) 

    
    return render (request,'bankdets/home.html',{'services':services})

def account(request):
    return render(request,'bankdets/account.html')

def internetBanking(request):
    return render(request,'internetBanking/loginpage.html')

def cards(request):
    return render(request,'bankdets/account.html')

def insurance(request):
    return render(request,'bankdets/account.html')

def investments(request):
    return render(request,'bankdets/account.html')

def support(request):
    return render(request,'bankdets/account.html')
