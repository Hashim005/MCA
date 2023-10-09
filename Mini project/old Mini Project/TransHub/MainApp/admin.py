from django.contrib import admin
from . models import Users
from django.contrib.auth.admin import UserAdmin



class CustomUserAdmin(UserAdmin):
    list_display=('username','email','phone_number')

admin.site.register(Users,CustomUserAdmin)

