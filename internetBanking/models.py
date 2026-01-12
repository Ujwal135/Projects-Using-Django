
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Customer_information
from django.utils import timezone
import uuid


# internet banking model 

class InternetBanking(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    customer = models.OneToOneField(Customer_information,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Internet Banking - {self.user.username}"



# Transaction internet baking model 


class Ibtransactions(models.Model):
    
    class Transaction_types(models.TextChoices):
        Credit = "CR","Credit"
        Debit = "DBT","Debit"
 
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    
    transaction_type = models.CharField(
        max_length=3,
        choices=Transaction_types.choices,
        default=Transaction_types.Debit
    )
    
    receiver_account = models.CharField(
        max_length=20
        )
    
    sender_account = models.CharField(
        max_length=20
    )

    date_time = models.DateTimeField(
         auto_now_add=True,
         
    )
    
    transaction_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    
    balance_after = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    
    remark = models.CharField(
        max_length=30,
    )
   

