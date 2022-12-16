from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Valid email address required.')
    
    class Meta:
        model =CustomUser
        # fields =['username', 'email']
        fields = ['first_name', 'last_name', 'username', 'email']


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields =['username','email']
        

class EditUserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Valid email address required.')

    class Meta:
        model =CustomUser
        fields = ['first_name', 'last_name', 'username', 'email',]
    
    
    