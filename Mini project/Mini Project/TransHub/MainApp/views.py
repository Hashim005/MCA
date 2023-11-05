from collections import UserDict
import json
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import Category, Users
from TransHub.settings import EMAIL_HOST_USER
from .models import Users
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib import messages
from .models import Users, UserProfile

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
            role='user'
            
            if password != confirm_password:
                 return render(request, SignUp.html)
            user = Users(username=username,phone_number=phone, email=email,role=role)
            # password set
            user.set_password(password)
            #save the user to database
            user.save()
            UserProfile.objects.create(user=user)
            
            subject = 'Hello, '+username
            message = 'Your registration has been Successfully completed'
            from_email = EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect('login')
            
    return render(request,'SignUp.html')

def Log(request):
    if request.method == "POST":
         username = request.POST['username']
         user_password = request.POST['password']
         if username == "admin" and user_password == "admin":
              request.session['username'] = username
              return redirect("Admin_Home")
         
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


def check_username(request):
     username = request.GET.get('username', '')
     user_exits = Users.objects.filter(username=username).exists()
     return JsonResponse({'exists': user_exits})

def check_email(request):
     email = request.GET.get('email', '').lower
     email_exists = Users.objects.filter(email=email).exists()
     return JsonResponse({'exists': email_exists})

def Staff_signUp(request):
    if request.method == 'POST':
        # Similar to the SignUp view, include the role field
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST.get('phone')
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        role = 'Staff'  # Set the role to 'staff' for staff registration

        if password != confirm_password:
            return render(request, 'StaffSignUp.html')

        user = Users(username=username, phone_number=phone, email=email, role=role)
        user.set_password(password)
        user.save()
        return redirect('login')

    return render(request, 'StaffSignUp.html')

def Admin_Home(request):
     return render(request, 'adminhome.html')

def user_account(request):
    role_filter = request.GET.get('role')
    users = Users.objects.filter(~Q(is_superuser=True))  # Exclude superusers by default

    if role_filter:
        users = users.filter(role=role_filter)

    context = {'User_profiles': users, 'role_filter': role_filter}
    return render(request, 'usertable.html', context)

from django.template.loader import render_to_string
from django.utils.html import strip_tags


#def ActivateAccount(request):
#     return render(request, 'activate.html')

def activate_user(request, user_id):
    user = get_object_or_404(Users, id=user_id)

    if not user.is_active:
        user.is_active = True
        user.save()
        messages.success(request, f"User '{user.username}' has been activated by the admin, and an email has been sent.")
        
        # Send activation email to the user
        subject = "Account Activation"
        html_message = render_to_string('activation_email.html', {'user': user})
        plain_message = strip_tags(html_message)
        from_email = "transhubcorporationltd@gmail.com"  # Update with your email
        recipient_list = [user.email]
        send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)

    else:
        messages.warning(request, f"User '{user.username}' is activated.")

    return redirect('user_account')


def activatation_email(request):
     return render(request, 'activation_email.html')

def deactivate_user(request, user_id):
    user = get_object_or_404(Users, id=user_id)
    if user.is_active:
        user.is_active = False
        user.save()

        # Send deactivation email
        subject = 'Account Deactivation'
        message = 'Your account has been deactivated by the admin.'
        from_email = 'transhubcorporationltd@gmail.com'  # Replace with your email
        recipient_list = [user.email]
        html_message = render_to_string('deactivation_email.html', {'user': user})

        send_mail(subject, message, from_email, recipient_list, html_message=html_message)

        messages.success(request, f"User '{user.username}' has been deactivated, and an email has been sent.")
    else:
        messages.warning(request, f"User '{user.username}' is deactivated.")
    return redirect('user_account')

def deactivation_email(request):
     return render(request, 'deactivation_email.html')

# views.py
# views.py
from django.shortcuts import render, redirect
from .forms import SaveCategory, UserProfileForm, AdditionalProfileForm

def update_profile(request):
    # Check if the UserProfile exists for the user, and create it if it doesn't
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile(user=request.user)
        user_profile.save()

    user_form = UserProfileForm(request.POST, instance=request.user)
    profile_form = AdditionalProfileForm(request.POST, request.FILES, instance=user_profile)

    if request.method == 'POST':
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserProfileForm(instance=request.user)
        profile_form = AdditionalProfileForm(instance=user_profile)

    return render(request, 'update_profile.html', {'user_form': user_form, 'profile_form': profile_form})


def profile(request):
    return render(request, 'profile.html')

#context text
context = {
    'page_title' : 'File Management System',
}

#category
@login_required
def category_mgt(request):
    context['page_title'] = "Bus Categories"
    categories = Category.objects.all()
    context['categories'] = categories

    return render(request, 'category_mgt.html', context)

#save_category
@login_required
def save_category(request):
    resp = {'status':'failed','msg':''}
    if request.method == 'POST':
        if (request.POST['id']).isnumeric():
            category = Category.objects.get(pk=request.POST['id'])
        else:
            category = None
        if category is None:
            form = SaveCategory(request.POST)
        else:
            form = SaveCategory(request.POST, instance= category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category has been saved successfully.')
            resp['status'] = 'success'
        else:
            for fields in form:
                for error in fields.errors:
                    resp['msg'] += str(error + "<br>")
    else:
        resp['msg'] = 'No data has been sent.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

#manage_category
@login_required
def manage_category(request, pk=None):
    context['page_title'] = "Manage Category"
    if not pk is None:
        category = Category.objects.get(id = pk)
        context['category'] = category
    else:
        context['category'] = {}

    return render(request, 'manage_category.html', context)

#delete_category
@login_required
def delete_category(request):
    resp = {'status':'failed', 'msg':''}

    if request.method == 'POST':
        try:
            category = Category.objects.get(id = request.POST['id'])
            category.delete()
            messages.success(request, 'Category has been deleted successfully')
            resp['status'] = 'success'
        except Exception as err:
            resp['msg'] = 'Category has failed to delete'
            print(err)

    else:
        resp['msg'] = 'Category has failed to delete'
    
    return HttpResponse(json.dumps(resp), content_type="application/json")



