
from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Bus, Category, Location, UserProfile,Users

class UserProfileForm(UserChangeForm):
    class Meta:
        model = Users
        fields = ['phone_number']

class AdditionalProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'gender', 'city', 'date_of_birth', 'profile_picture']

class SaveCategory(forms.ModelForm):
    name = forms.CharField(max_length="250")
    description = forms.Textarea()
    status = forms.ChoiceField(choices=[('1','Active'),('2','Inactive')])

    class Meta:
        model = Category
        fields = ('name','description','status')

    def clean_name(self):
        id = self.instance.id if self.instance.id else 0
        name = self.cleaned_data['name']
        # print(int(id) > 0)
        # raise forms.ValidationError(f"{name} Category Already Exists.")
        try:
            if int(id) > 0:
                category = Category.objects.exclude(id=id).get(name = name)
            else:
                category = Category.objects.get(name = name)
        except:
            return name
            # raise forms.ValidationError(f"{name} Category Already Exists.")
        raise forms.ValidationError(f"{name} Category Already Exists.")
    
class SaveLocation(forms.ModelForm):
    location = forms.CharField(max_length="250")
    status = forms.ChoiceField(choices=[('1','Active'),('2','Inactive')])

    class Meta:
        model = Location
        fields = ('location','status')

    def clean_location(self):
        id = self.instance.id if self.instance.id else 0
        location = self.cleaned_data['location']
        # print(int(id) > 0)
        try:
            if int(id) > 0:
                loc = Location.objects.exclude(id=id).get(location = location)
            else:
                loc = Location.objects.get(location = location)
        except:
            return location
            # raise forms.ValidationError(f"{location} Category Already Exists.")
        raise forms.ValidationError(f"{location} Location Already Exists.")

class SaveBus(forms.ModelForm):
    bus_number = forms.CharField(max_length="250")
    category = forms.CharField(max_length="250")
    seats = forms.CharField(max_length="250")
    status = forms.ChoiceField(choices=[('1','Active'),('2','Inactive')])
    print(bus_number)
    class Meta:
        model = Bus
        fields = ('bus_number','category','seats','status')

    def clean_category(self):
        id = self.cleaned_data['category']
        try:
            category = Category.objects.get(id = id)
            return category
        except:
            raise forms.ValidationError(f"Invalid Category Already Exists.")
    
    def clean_bus_number(self):
        id = self.instance.id if self.instance.id else 0
        bus_number = self.cleaned_data['bus_number']
        # print(int(id) > 0)
        try:
            if int(id) > 0:
                bus = Bus.objects.exclude(id=id).get(bus_number = bus_number)
            else:
                bus = Bus.objects.get(bus_number = bus_number)
        except:
            return bus_number
            # raise forms.ValidationError(f"{bus_number} Category Already Exists.")
        raise forms.ValidationError(f"{bus_number} bus Already Exists.")
