from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, null=False)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="customer")

    def __str__(self):
        return self.user.username


