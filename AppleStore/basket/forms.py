from django import forms

from About.models import Order


class BasketAddProductForm(forms.Form):
    count = forms.IntegerField(min_value=1, initial=1, label='Количество',
                               widget=forms.NumberInput(attrs={'class': 'form-control'}))
    reload = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


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