from django.db import models
from django.utils import timezone
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
    
class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=(('1', 'Active'), ('2', 'Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    location = models.CharField(max_length=250)
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location
    
class Bus(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, blank= True, null = True)
    bus_number = models.CharField(max_length=250)
    seats = models.FloatField(max_length=5, default=0)
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bus_number
    
class Schedule(models.Model):
    code = models.CharField(max_length=100)
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE)
    depart = models.ForeignKey(Location,on_delete=models.CASCADE, related_name='depart_location')
    destination = models.ForeignKey(Location,on_delete=models.CASCADE, related_name='destination')
    schedule= models.DateTimeField()
    fare= models.FloatField()
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Cancelled')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.code + ' - ' + self.bus.bus_number)


class Seat_map(models.Model):
    seat_number = models.CharField(max_length=10, primary_key=True)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    booked_seat = models.BooleanField(default=False)
    booked_by = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.seat_number} - {self.bus} - {self.schedule}"


from django.db import models

class Feedback(models.Model):
    User = models.ForeignKey(Users, on_delete=models.CASCADE)  # Assuming you have a User model
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Booking(models.Model):
    book_id = models.AutoField(primary_key=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    passenger_name = models.CharField(max_length=255, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email_id = models.EmailField(unique=True, null=True)
    seat_no = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    total_price = models.CharField(max_length=10, blank=True, null=True)  # Example field for total price
    seat_no_count = models.IntegerField(default=0)  # Field to store the count of selected seats

    def __str__(self): 
        return f"Booking ID: {self.book_id} - Passenger: {self.passenger_name} - Schedule: {self.schedule}"


    
