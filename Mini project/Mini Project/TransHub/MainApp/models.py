from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    class Role(models.TextChoices):
        ADMIN="ADMIN",'Admin'
        STAFF="STAFF",'Staff'
        USER="UAER",'User'
        
    role=models.CharField(max_length=15,default=0)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.email
    
