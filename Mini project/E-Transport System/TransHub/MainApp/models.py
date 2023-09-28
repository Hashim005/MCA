   
from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    email = models.EmailField(max_length=246, default="")
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.email
    
