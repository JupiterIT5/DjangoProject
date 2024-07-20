from django.core.exceptions import ValidationError
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import re

MAX_LENGTH = 255

class SupplierForm(forms.Form):
    name = forms.CharField(max_length=MAX_LENGTH, label='Название компании')
    agent_lastname = forms.CharField(max_length=MAX_LENGTH, label='Фамилия представителя')
    agent_name = forms.CharField(max_length=MAX_LENGTH, label='Имя представителя')
    agent_surname = forms.CharField(max_length=MAX_LENGTH, label='Отчество представителя')
    phone = forms.CharField(max_length=16, label='Телефон представителя')
    location = forms.CharField(max_length=MAX_LENGTH, label='Адрес')
    
    name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Название компании'})
    agent_lastname.widget.attrs.update({'class': 'form-control', 'placeholder': 'Фамилия'})
    agent_name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Имя'})
    agent_surname.widget.attrs.update({'class': 'form-control', 'placeholder': 'Отчество'})
    phone.widget.attrs.update({'class': 'form-control', 'placeholder': 'Телефон'})
    location.widget.attrs.update({'class': 'form-control', 'placeholder': 'Адрес'})
    
    def clean_telephone(self):
        phone = self.cleaned_data['phone']
        if re.match(r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}', phone.replace(' ', '')):
            return phone
        return False
    

class ProductForm(forms.Form):
    name = forms.CharField(min_length=10, max_length=MAX_LENGTH, label='Название')
    price = forms.FloatField(label='Цена')
    
    name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Название'})
    price.widget.attrs.update({'class': 'form-control', 'placeholder': 'Цена'})
    
    
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
            label='Логин пользователя',
            widget=forms.TextInput(attrs={'class': 'form-control',}),
            min_length=2
        )
        email = forms.EmailField(
            label='Электронная почта',
            widget=forms.EmailInput(attrs={'class': 'form-control'})
        )
        password1 = forms.CharField(
            label='Введите пароль',
            widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )
        password2 = forms.CharField(
            label='Повторите пароль',
            widget=forms.PasswordInput(attrs={'class': 'form-control'})
        )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Введите логин',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        min_length=2
    )
    
    password = forms.CharField(
        label='Введите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'buyer_lastname',
            'buyer_name',
            'buyer_surname',
            'comment',
            'location',
            'delivery',
            'product',
        )

        buyer_lastname = forms.CharField(
            min_length=3,
            label=forms.TextInput(attrs={'class': 'form-control'})
        )
        buyer_name = forms.CharField(
            min_length=3,
            label=forms.TextInput(attrs={'class': 'form-control'})
        )
        buyer_surname = forms.CharField(
            min_length=3,
            label=forms.TextInput(attrs={'class': 'form-control'})
        )
        comment = forms.CharField(
            min_length=1,
            label=forms.TextInput(attrs={'class': 'form-control'})
        )
        location = forms.CharField(
            min_length=1,
            label=forms.TextInput(attrs={'class': 'form-control'})
        )
        delivery = forms.CharField(
            min_length=2,
            label=forms.TextInput(attrs={'class': 'form-control'})
        )
        
        buyer_lastname.widget.attrs.update({'placeholder': 'Введите фамилию'})
        buyer_name.widget.attrs.update({'placeholder': 'Введите имя'})
        buyer_surname.widget.attrs.update({'placeholder': 'Введите отчество'})
        comment.widget.attrs.update({'placeholder': 'Введите комментарий'})
        location.widget.attrs.update({'placeholder': 'Введите адрес доставки'})
        delivery.widget.attrs.update({'placeholder': 'Укажите способ доставки'})
        
        
        