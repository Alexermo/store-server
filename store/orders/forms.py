from django import forms

from .models import Order


class OrderForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': "Введите имя", }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': "Введите фамилию"}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': "form-control", 'placeholder': "Введите email"}))
    adress = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Введите адресс доставки"}))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'adress')
