from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=150, label='Last Name')
    DOB = forms.DateField(label='Date Of Birth')
    PhoneNumber = forms.CharField(max_length=15, label='Phone Number')
    Address = forms.CharField(max_length=150, label='Address ')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.DOB = self.cleaned_data['DOB']
        user.PhoneNumber = self.cleaned_data['PhoneNumber']
        user.Address = self.cleaned_data['Address']
        user.save()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')
