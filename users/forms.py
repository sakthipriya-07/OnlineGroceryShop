from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Customer, User


class CustomerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'username', 'password1', 'password2')

    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        Customer.objects.create(user=user)
        return user


class CustomerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone')


