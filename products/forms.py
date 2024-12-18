from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "quantity"]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["quantity"]
