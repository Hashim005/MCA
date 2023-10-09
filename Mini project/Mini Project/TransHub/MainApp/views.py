from collections import UserDict
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from TransHub.settings import EMAIL_HOST_USER
from .models import Users
from django.core.mail import send_mail
# from django.http import HttpResponse

@never_cache
def showIndex(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@csrf_protect
def SignUp(request):
    if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            phone = request.POST.get('phone')
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            
            if password != confirm_password:
                 return render(request, SignUp.html)
            user = Users(username=username,phone_number=phone, email=email)
            # password set
            user.set_password(password)
            #save the user to database
            user.save()
            return redirect('login')
            
    return render(request,'SignUp.html')

def Log(request):
    if request.method == "POST":
         username = request.POST['username']
         user_password = request.POST['password']
         
         user = authenticate(username=username, password=user_password)
         
         if user is not None:
              login(request, user)
              return redirect('Home')
         else:
              return render(request, 'login.html', {'Error_message': 'invalid creadential!!'})
    
    return render(request,'login.html')
    
def logout_user(request):
     if request.user.is_authenticated:
          logout(request)
     return redirect('showindex')   

import random
def generateOTP():
     generatedOTP = "".join(str(random.randint(0, 9)) for _ in range(6))
     return generatedOTP


#@login_required(login_url='login')
@never_cache
def Home(request):
     return render(request, 'home.html')

def validateGlobalEmail(request):
     email = request.GET['email']
     cpnm = "TransHub Corp. Ltd."
     otp = generateOTP()
     subject = 'Hello, Django Email!'
     message = 'Here is Your OTP.'+otp
     from_email = EMAIL_HOST_USER
     recipient_list = [email] 
     data = {
          "exists": send_mail(subject, message, f"{cpnm} <{from_email}>", recipient_list),
          "otp": otp
     }
     return JsonResponse(data)