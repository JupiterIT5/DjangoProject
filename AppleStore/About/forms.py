from django import forms
from .models import *
import re

MAX_LENGTH = 255


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'tag',
            'name',
            'price',
            'category',
            'description'
        )
        
        name = forms.CharField(
            min_length=2, 
            max_length=MAX_LENGTH,
            label=forms.TextInput(attrs={'class': 'form-control'})    
        )
        price = forms.FloatField(
            min_value=1,
            max_value=1000000,
            label=forms.TextInput(attrs={'class': 'form-control'})    
        )
        description = forms.CharField(
            min_length=2,
            label=forms.TextInput(attrs={'class': 'form-control'})    
        )
        category = forms.ChoiceField()
        tag = forms.ChoiceField()


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = (
            'name',
            'agent_lastname',
            'agent_name',
            'agent_surname',
            'phone',
            'location'
        )
        
        name = forms.CharField(max_length=MAX_LENGTH, label='Название компании', widget=forms.TextInput(attrs={'class': 'form-control'}))
        agent_lastname = forms.CharField(max_length=MAX_LENGTH, label='Фамилия представителя', widget=forms.TextInput(attrs={'class': 'form-control'}))
        agent_name = forms.CharField(max_length=MAX_LENGTH, label='Имя представителя', widget=forms.TextInput(attrs={'class': 'form-control'}))
        agent_surname = forms.CharField(max_length=MAX_LENGTH, label='Отчество представителя', widget=forms.TextInput(attrs={'class': 'form-control'}))
        phone = forms.CharField(max_length=16, label='Телефон представителя', widget=forms.TextInput(attrs={'class': 'form-control'}))
        location = forms.CharField(max_length=MAX_LENGTH, label='Адрес', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    def clean_telephone(self):
        phone = self.cleaned_data['phone']
        if re.match(r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}', phone.replace(' ', '')):
            return phone
        return False
    

class OrderForm(forms.ModelForm):
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