from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    class Role(models.TextChoices):
        ADMIN="ADMIN",'Admin'
        STAFF="STAFF",'Staff'
        USER="USER",'User'
        
    role=models.CharField(max_length=15,default='USER')
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.email
    
class UserProfile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)


    def __str__(self):
        return self.user.username
    