from django.db import models


# Create your models here.
import uuid

class Customer_information(models.Model):
    
    Gender_type = (
        ("male","Male"),
        ("female","Female")
    )
    customer_id = models.CharField(max_length=20, unique=True,blank=True)
    first_name = models.CharField( max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=12,choices=Gender_type )
    email_id = models.EmailField(max_length=30) 
    mobile = models.CharField(max_length=13)
    address = models.CharField(max_length=70)
    pincode = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    aadhar_no = models.CharField(max_length=20)
    ac_created = models.DateField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.customer_id:
            
            last_customer = Customer_information.objects.order_by('-id').first()

            if last_customer and last_customer.customer_id:
                last_number = int(last_customer.customer_id.replace('SUPR', ''))
                next_number = last_number + 1
            else:
                next_number = 1
    
            self.customer_id = f"SUPR{str(next_number).zfill(6)}"
    
        super().save(*args, **kwargs)   
        
    def __str__(self):
        return self.customer_id
       
    
  
# create new inharitance .

class Account(models.Model):
    class ACCOUNTTYPE(models.TextChoices):
        SAVINGS = 'savings', 'Savings'
        CURRENT = 'current', 'Current'
        
    
    customer = models.ForeignKey(Customer_information,
                                 on_delete=models.CASCADE,
                                 related_name='accounts')
    account_number = models.CharField(max_length=20,editable=False,unique=True)
    account_type = models.CharField(max_length=25,choices=ACCOUNTTYPE,default=ACCOUNTTYPE.SAVINGS)
    balance = models.DecimalField(max_digits=12,decimal_places=2,default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f"{self.customer.first_name}  {self.customer.last_name} - {self.account_number}"
    
    def save(self,*args, **kwargs):
        if not self.account_number:
            self.account_number = self.uniqueid_function()
            
        super().save(*args,**kwargs)

    def uniqueid_function(self):
        actype = 'SAV' if self.account_type == Account.ACCOUNTTYPE.SAVINGS else 'CUR'
        fixedstr = 'SUPR'
        unique_part = self.uuid_numeric_4()
        return f'{actype}-{fixedstr}-{unique_part}'
    
    
    def uuid_numeric_4(self):
        return str(uuid.uuid4().int)[-4:]