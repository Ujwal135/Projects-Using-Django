
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Customer_information
from django.utils import timezone

# internet banking model 

class InternetBanking(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    customer = models.OneToOneField(Customer_information,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Internet Banking - {self.user.username}"

# Create your models here.
