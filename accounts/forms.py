from django.forms import ModelForm
from .models import Customer_information
from django import forms  

class Customer_Form(forms.ModelForm):
    class Meta:
        model = Customer_information
        fields = [
            'first_name','last_name','gender','mobile','email_id','date_of_birth','address','pincode','aadhar_no']
        widgets = {
            "first_name": forms.TextInput(attrs={
                "placeholder": "Enter first name",
                "class": "w-full rounded-lg border-gray-300 focus:ring-indigo-500"
            }),
            "last_name": forms.TextInput(attrs={
                "placeholder": "Enter last name",
                "class": "w-full rounded-lg border-gray-300 focus:ring-indigo-500"
            }),
            "mobile": forms.NumberInput(attrs={
                "placeholder": "Enter mobile number",
                "class": "w-full rounded-lg border-gray-300"
            }),
            'date_of_birth': forms.DateInput(attrs={
                    'type': 'date', 
                    'class': 'w-full rounded-lg border-gray-300 focus:ring-indigo-500'
                }
            )
        }
            
        

