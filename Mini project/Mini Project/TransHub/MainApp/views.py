from collections import UserDict
import json
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import Bus, Category, Location, Schedule, Users
from TransHub.settings import EMAIL_HOST_USER
from .models import Users
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib import messages
from .models import Users, UserProfile
from datetime import datetime

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
         user = authenticate(username=username, password=user_password)
         if user is not None:
            if user.is_superuser:
                login(request, user)
                request.session['username'] = username
                return redirect("Admin_Home")
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
     if not request.user.is_authenticated:
         return redirect ('login')
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
from .forms import SaveBus, SaveCategory, SaveLocation, SaveSchedule, UserProfileForm, AdditionalProfileForm

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

# Location
@login_required
def location_mgt(request):
    context['page_title'] = "Locations"
    locations = Location.objects.all()
    context['locations'] = locations

    return render(request, 'location_mgt.html', context)

#save location
@login_required
def save_location(request):
    resp = {'status':'failed','msg':''}
    if request.method == 'POST':
        if (request.POST['id']).isnumeric():
            location = Location.objects.get(pk=request.POST['id'])
        else:
            location = None
        if location is None:
            form = SaveLocation(request.POST)
        else:
            form = SaveLocation(request.POST, instance= location)
        if form.is_valid():
            form.save()
            messages.success(request, 'Location has been saved successfully.')
            resp['status'] = 'success'
        else:
            for fields in form:
                for error in fields.errors:
                    resp['msg'] += str(error + "<br>")
    else:
        resp['msg'] = 'No data has been sent.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

#manage location
@login_required
def manage_location(request, pk=None):
    context['page_title'] = "Manage Location"
    if not pk is None:
        location = Location.objects.get(id = pk)
        context['location'] = location
    else:
        context['location'] = {}

    return render(request, 'manage_location.html', context)

#delete location
@login_required 
def delete_location(request):
    resp = {'status':'failed', 'msg':''}

    if request.method == 'POST':
        try:
            location = Location.objects.get(id = request.POST['id'])
            location.delete()
            messages.success(request, 'Location has been deleted successfully')
            resp['status'] = 'success'
        except Exception as err:
            resp['msg'] = 'location has failed to delete'
            print(err)

    else:
        resp['msg'] = 'location has failed to delete'
    
    return HttpResponse(json.dumps(resp), content_type="application/json")

# bus
@login_required
def bus_mgt(request):
    context['page_title'] = "Buses"
    buses = Bus.objects.all()
    context['buses'] = buses

    return render(request, 'bus_mgt.html', context) 

@login_required
def save_bus(request):
    resp = {'status':'failed','msg':''}
    if request.method == 'POST':
        if (request.POST['id']).isnumeric():
            bus = Bus.objects.get(pk=request.POST['id'])
        else:
            bus = None
        if bus is None:
            form = SaveBus(request.POST)
        else:
            form = SaveBus(request.POST, instance= bus)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bus has been saved successfully.')
            resp['status'] = 'success'
        else:
            for fields in form:
                for error in fields.errors:
                    resp['msg'] += str(error + "<br>")
    else:
        resp['msg'] = 'No data has been sent.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

@login_required
def manage_bus(request, pk=None):
    context['page_title'] = "Manage Bus"
    categories = Category.objects.filter(status = 1).all()
    context['categories'] = categories
    if not pk is None:
        bus = Bus.objects.get(id = pk)
        context['bus'] = bus
    else:
        context['bus'] = {}

    return render(request, 'manage_bus.html', context)

@login_required
def delete_bus(request):
    resp = {'status':'failed', 'msg':''}

    if request.method == 'POST':
        try:
            bus = Bus.objects.get(id = request.POST['id'])
            bus.delete()
            messages.success(request, 'Bus has been deleted successfully')
            resp['status'] = 'success'
        except Exception as err:
            resp['msg'] = 'bus has failed to delete'
            print(err)

    else:
        resp['msg'] = 'bus has failed to delete'
    
    return HttpResponse(json.dumps(resp), content_type="application/json")

# schedule
@login_required
def schedule_mgt(request):
    context['page_title'] = "Trip Schedules"
    schedules = Schedule.objects.all()
    context['schedules'] = schedules

    return render(request, 'schedule_mgt.html', context)

@login_required
def save_schedule(request):
    resp = {'status':'failed','msg':''}
    if request.method == 'POST':
        if (request.POST['id']).isnumeric():
            schedule = Schedule.objects.get(pk=request.POST['id'])
        else:
            schedule = None
        if schedule is None:
            form = SaveSchedule(request.POST)
        else:
            form = SaveSchedule(request.POST, instance= schedule)
        if form.is_valid():
            form.save()
            messages.success(request, 'Schedule has been saved successfully.')
            resp['status'] = 'success'
        else:
            for fields in form:
                for error in fields.errors:
                    resp['msg'] += str(error + "<br>")
    else:
        resp['msg'] = 'No data has been sent.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

@login_required
def manage_schedule(request, pk=None):
    context['page_title'] = "Manage Schedule"
    buses = Bus.objects.filter(status = 1).all()
    locations = Location.objects.filter(status = 1).all()
    context['buses'] = buses
    context['locations'] = locations
    if not pk is None:
        schedule = Schedule.objects.get(id = pk)
        context['schedule'] = schedule
    else:
        context['schedule'] = {}

    return render(request, 'manage_schedule.html', context)

@login_required
def delete_schedule(request):
    resp = {'status':'failed', 'msg':''}

    if request.method == 'POST':
        try:
            schedule = Schedule.objects.get(id = request.POST['id'])
            schedule.delete()
            messages.success(request, 'Schedule has been deleted successfully')
            resp['status'] = 'success'
        except Exception as err:
            resp['msg'] = 'schedule has failed to delete'
            print(err)

    else:
        resp['msg'] = 'Schedule has failed to delete'
    
    return HttpResponse(json.dumps(resp), content_type="application/json") 


class Seat:
    def __init__(self, number, is_reserved, is_women_seat):
        self.number = number
        self.is_reserved = is_reserved
        self.is_women_seat = is_women_seat

def bus_seat_map(request):
    # Example: Creating a list of 40 seats with alternating reserved and available status,
    # and 5 women seats
    num_seats = 40
    num_women_seats = 5
    seats = [Seat(number=i, is_reserved=i % 2 == 0, is_women_seat=i < num_women_seats) for i in range(1, num_seats + 1)]

    return render(request, 'bus_grid_seat.html', {'seats': seats})

def book_seat(request):
    if request.method == 'POST':
        selected_seats = request.POST.getlist('selected_seats')
        # Handle booking logic here
        return HttpResponse(f'Selected Seats: {", ".join(selected_seats)}')
    else:
        return HttpResponse('Invalid request method')


# find trip set

from django.shortcuts import render
from django.http import Http404
from datetime import datetime
from .models import Location, Schedule

from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime
from .models import Schedule, Location

def find_trip(request):
    context = {}
    context['page_title'] = 'Find Trip Schedule'
    context['locations'] = Location.objects.filter(status=1).all()
    today = datetime.today().strftime("%Y-%m-%d")
    context['today'] = today

    if request.method == 'GET':
        depart = request.GET.get('depart')
        destination = request.GET.get('destination')
        journey_date = request.GET.get('journeyDate')
        return_date = request.GET.get('returnDate')

        # Basic input validation
        if not depart and not destination and not journey_date:
            context['error_message'] = 'Please provide at least one search parameter.'
            return render(request, 'find_trip.html', context)

        # Additional validation can be added here if needed

        # Validate depart and destination locations
        try:
            depart_location = Location.objects.get(pk=depart)
        except Location.DoesNotExist:
            raise Http404('Depart location does not exist')

        try:
            destination_location = Location.objects.get(pk=destination)
        except Location.DoesNotExist:
            raise Http404('Destination location does not exist')

        # Query Schedule model based on search parameters
        schedules = Schedule.objects.all()

        if depart:
            schedules = schedules.filter(depart=depart_location)
        if destination:
            schedules = schedules.filter(destination=destination_location)
        if journey_date:
            # Validate journey_date format (YYYY-MM-DD)
            try:
                journey_date = datetime.strptime(journey_date, '%Y-%m-%d').date()
            except ValueError:
                context['error_message'] = 'Invalid journey date format.'
                return render(request, 'find_trip.html', context)

            # Filter schedules for the selected journey_date
            schedules = schedules.filter(schedule__date__contains=journey_date)

        context['schedules'] = schedules

        # Render the schedule_view_page template with the filtered schedules
        return render(request, 'schedule_view_page.html', context)

    return render(request, 'find_trip.html', context)
def schedule_view_page(request):
    context = {}

    if request.method == 'GET': 
        depart = request.GET.get('depart')
        destination = request.GET.get('destination')
        journey_date = request.GET.get('journeyDate')

        # Additional validation can be added here if needed

        # Filter schedules based on the user's search parameters
        schedules = Schedule.objects.all()

        if depart:
            schedules = schedules.filter(depart__location__icontains=depart)

        if destination:
            schedules = schedules.filter(destination__location__icontains=destination)

        if journey_date:
            # Filter schedules for the selected journey_date
            schedules = schedules.filter(schedule__date__contains=journey_date)

        # Create a dictionary to store unique buses based on bus_number
        unique_buses = {}

        # Iterate through schedules and keep only the first occurrence of each bus
        for schedule in schedules:
            bus_number = schedule.bus.bus_number
            if bus_number not in unique_buses:
                unique_buses[bus_number] = schedule

        # Extract the unique schedules from the dictionary
        unique_schedules = list(unique_buses.values())

        context['schedules'] = unique_schedules

    return render(request, 'schedule_view_page.html', context)

from django.shortcuts import render, redirect
from .models import Feedback
from django.contrib.auth.decorators import login_required

@never_cache
@login_required(login_url="login")
def submit_feedback(request):
    if request.method == "POST":
        feedback_message = request.POST.get('feedback_message')
        if feedback_message:
            Feedback.objects.create(User=request.user, message=feedback_message)
            # You can add additional logic here (e.g., sending a confirmation email)
            return redirect('feedback_thankyou')

    return render(request, 'feedback_form.html')


def feedback_thankyou(request):
     return render(request,'feedback_thankyou.html')


from django.shortcuts import render
from .models import Feedback

def adminfeedback(request):
    feedback_list = Feedback.objects.all()
    return render(request, 'adminfeedback.html', {'feedback_list': feedback_list})

















    




