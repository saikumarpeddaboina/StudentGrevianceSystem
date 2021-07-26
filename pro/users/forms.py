from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AuthForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['branch',]
