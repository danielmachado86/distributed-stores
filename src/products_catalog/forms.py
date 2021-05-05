from django import forms
from django.forms import fields

from .models import Category, Product, Brand, ProductSpecs

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

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = [
            'name',
            'description',
            'picture'
        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
            'parent',
            'description',
            'picture'
        ]

class ProductSpecsForm(forms.ModelForm):
    class Meta:
        model = ProductSpecs
        fields = [
            'attribute',
            'value',
        ]