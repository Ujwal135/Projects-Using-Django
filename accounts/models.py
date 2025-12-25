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
    
            if last_customer:
                last_number = int(last_customer.customer_id[4:])
                next_number = last_number + 1
            else:
                next_number = 1
    
            self.customer_id = "SUPR" + str(next_number).zfill(6)
    
        super().save(*args, **kwargs)   
        
    def __str__(self):
        return self.customer_id
       
    
  
# create new inharitance .

class Account(models.Model):
    
    customer = models.ForeignKey(Customer_information,
                                 on_delete=models.CASCADE,
                                 related_name='accounts')
    account_type = (
                    ('SAVING','Saving account'),
                    ('CURRENT', 'Current Account'),
                    )
    account_number = models.CharField(max_length=20,editable=False,unique=True)
    balance = models.DecimalField(max_digits=12,decimal_places=2,default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self,*args, **kwargs):
        if not self.account_number:
            self.account_number = self.uniqueid_function()
            
        super().save(*args,**kwargs)

    def uniqueid_function(self):
        
        actype = 'SAV' if self.account_type == 'SAVING' else 'CUR'  

        fixedstr = 'SUPR'
        
        unique_part = self.uuid_numeric_4()
               
        return f'{actype}+{fixedstr}+{unique_part}'  
    
    
    def uuid_numeric_4():
        return str(uuid.uuid4().int)[-4:]