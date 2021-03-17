from django import forms
from django.forms import fields

from .models import Product, ProductSpecs

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'brand',
            'category',
            'description',
            'picture'
        ]

class ProductSpecsForm(forms.ModelForm):
    class Meta:
        model = ProductSpecs
        fields = [
            'product',
            'attribute',
            'value',
        ]