from django.db import models


# Create your models here.

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
    Date_of_birth = models.DateField
    aadhar_no = models.IntegerField(max_length=20)
    
    def save(self, *args, **kwargs):
        if self.customer_id == "":
            
            last_customer = Customer_information.objects.last()
            
            if last_customer is None:
                next_number = 1
            else:
                last_number = int(last_customer.customer_id[4:])
                next_number = last_number + 1
            
            self.customer_id = "SUPR" + str(next_number).zfill(6)
            
        super().save(*args, **kwargs)   
       
  
       