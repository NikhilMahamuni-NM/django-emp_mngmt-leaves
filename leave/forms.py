from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Leave

class RegisterUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        

class LeaveForm(forms.ModelForm):

    class Meta:
        model = Leave
        fields = '__all__'
    
