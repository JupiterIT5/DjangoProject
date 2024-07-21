from django.core.exceptions import ValidationError
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import re

MAX_LENGTH = 255

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = (
            'name', 
            'agent_lastname',
            'agent_name',
            'agent_surname',
            'phone',
            'location',
        )
        
        name = forms.CharField(max_length=MAX_LENGTH, label='Название компании', widget=forms.TextInput(attrs={'class': 'form-control'}))
        agent_lastname = forms.CharField(max_length=MAX_LENGTH, label='Фамилия представителя', widget=forms.TextInput(attrs={'class': 'form-control'}))
        agent_name = forms.CharField(max_length=MAX_LENGTH, label='Имя представителя', widget=forms.TextInput(attrs={'class': 'form-control'}))
        agent_surname = forms.CharField(max_length=MAX_LENGTH, label='Отчество представителя', widget=forms.TextInput(attrs={'class': 'form-control'}))
        phone = forms.CharField(max_length=16, label='Телефон представителя')
        location = forms.CharField(max_length=MAX_LENGTH, label='Адрес', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    def clean_telephone(self):
        phone = self.cleaned_data['phone']
        if re.match(r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}', phone.replace(' ', '')):
            return phone
        return False
    
class SupplyForm(forms.ModelForm):
    class Meta:
        model = PosSupply
        fields = (
            'product',
            'supply',
            'count'
        )
        product = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        supply = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        count = forms.IntegerField(min_value = 1, widget=forms.TextInput(attrs={'class': 'form-control'}))
    

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