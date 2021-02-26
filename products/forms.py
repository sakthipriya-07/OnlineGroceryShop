from django import forms
from django.contrib.auth.models import User
from .models import Product, Feedback, Category
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'name', 'slug', 'image', 'description', 'price', 'available')


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'subject', 'description')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'slug')
