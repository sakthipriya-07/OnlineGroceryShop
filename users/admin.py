from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.admin import UserAdmin
from .models import Customer, User


class CustomerList(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone')

    def username(self, instance):  # name of the method should be same as the field given in `list_display`
        try:
            return instance.user.username
        except ObjectDoesNotExist:
            return 'ERROR!!'

    def first_name(self, instance):
        try:
            return instance.user.first_name
        except ObjectDoesNotExist:
            return 'ERROR!!'

    def last_name(self, instance):
        try:
            return instance.user.last_name
        except ObjectDoesNotExist:
            return 'ERROR!!'

    def email(self, instance):
        try:
            return instance.user.email
        except ObjectDoesNotExist:
            return 'ERROR!!'

    def phone(self, instance):
        try:
            return instance.user.phone
        except ObjectDoesNotExist:
            return 'ERROR!!'


admin.site.register(Customer, CustomerList)
admin.site.register(User, UserAdmin)
