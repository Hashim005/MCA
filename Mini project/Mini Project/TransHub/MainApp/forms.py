
from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile,Users

class UserProfileForm(UserChangeForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'phone_number']

class AdditionalProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'gender', 'city', 'date_of_birth', 'profile_picture']
