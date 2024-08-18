from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )
        username = forms.CharField(
            label='Имя',
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
        
        email = forms.EmailField(
            label='Email',
            widget=forms.EmailInput(attrs={'class': 'form-control'})
        )
        
        password1 = forms.CharField(
            label='Пароль',
            widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )
        
        password2 = forms.CharField(
            label='Повторите пароль',
            widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Введите логин',
        widget=forms.TextInput({'class': 'form-control'}),
        min_length=2
    )
    
    password = forms.CharField(
        label='Введите пароль',
        widget=forms.PasswordInput({'class': 'form-control'}),
    )