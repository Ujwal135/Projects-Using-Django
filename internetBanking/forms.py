from django import forms



class InternetBankingRegisterUser(forms.Form):
    
    customer_id = forms.CharField( 
                max_length=12,
                label=" Customer_id")
    
    account_number =forms.CharField(
        max_length=20,
        label="account_number")
    
    
    mobile_number = forms.CharField(
        max_length=10,
        label='Mobile Number')
    
    username = forms.CharField(
        max_length = 50,
        label='Username')
    
    password = forms.CharField(
        widget = forms.PasswordInput,
        label="Password ")
    
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        label= " Confirm Password"
    )
    
    
    def clean_mobile_number(self):
        mobile = self.cleaned_data.get("mobile_number")
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError("Enter a valid 10-digit mobile number")
        return mobile

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data




class Banktobanktransfer(forms.Form):
    
    account_number = forms.CharField(
        max_length=20,
        required= True,
        label="account_number"
    )
    
    confirm_account = forms.CharField(
        max_length=20,
        required= True,
        label="confirm_account"
    )
    
    receiver_name = forms.CharField(
     max_length=20,
     required=True,
     label="receiver_name"   
    )
    
    mobile = forms.CharField(
        max_length=10,
        required=True,
        label="mobile"
    )
    
    customer_id = forms.CharField(
        max_length=15,
        required=True,
        label="customer_id"
    )
    
    amount = forms.DecimalField(
        required = True,
        label="amount",
        decimal_places=2,
        min_value=1,
        max_digits=20
    )
    
    def clean(self):
        cleaned_data = super().clean()
        acc = cleaned_data.get("account_number")
        confirm = cleaned_data.get("confirm_account")

        if acc and confirm and acc != confirm:
            raise forms.ValidationError(
                "Account numbers do not match"
            )

        return cleaned_data
    
    def clean_mobile(self):
        mobile = self.cleaned_data.get("mobile")

        if not mobile.isdigit():
            raise forms.ValidationError("Mobile must contain digits only")

        if len(mobile) != 10:
            raise forms.ValidationError("Mobile number must be 10 digits")

        return mobile