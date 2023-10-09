from collections import UserDict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import Users
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

#@login_required(login_url='login')
@never_cache
def Home(request):
     return render(request, 'home.html')