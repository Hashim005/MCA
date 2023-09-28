from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from .models import *
# from django.http import HttpResponse


def showIndex(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

@csrf_protect
def SignUp(request):
    if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            phoneNum = request.POST.get('PhoneNum')
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            
            if password != confirm_password:
                 return render(request, SignUp.html)
            user = Users(username=username, email=email, phone_number=phoneNum)
            # password set
            user.set_password(password)
            #save the user to database
            user.save()
            return redirect('login')
            
    return render(request,'SignUp.html')

def Login(request):
    if request.method == "POST":
         user_email = request.POST["email"]
         user_password = request.POST["password"]
         user = authenticate(request, email=user_email, password=user_password)
         if user is not None:
              login(request, user)
              request.session['email'] = user.email
              return redirect('Home')
         else:
              return render(request, 'Login.html', {'Error_message': 'invalid creadential!!'})
    
    return render(request,'Login.html')
    
def logout_user(request):
     logout(request)
     return redirect('showindex')   

def Home(request):
     return render(request, 'home.html')