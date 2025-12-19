from django.shortcuts import render

# Create your views here.

    
def home(request):
    services = [
        {"title": "Accounts", "desc": "Safe and secure savings", "icon": "💰"},
        {"title": "Loans", "desc": "Quick loan approvals", "icon": "🏦"},
        {"title": "Cards", "desc": "Debit and credit cards", "icon": "💳"},
        {"title": "Insurance", "desc": "Life & health coverage", "icon": "🛡️"},
        {"title": "Investments", "desc": "Grow your wealth", "icon": "📈"},
        {"title": "Support", "desc": "24×7 customer support", "icon": "☎️"},
    ]

    # Add staggered animation delay
    for i, service in enumerate(services):
        service['delay'] = round(i * 0.15, 2) 

    
    return render (request,'bankdets/home.html',{'services':services})
