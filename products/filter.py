import django_filters
from django_filters import CharFilter, RangeFilter
from .models import *
from django.utils.translation import ugettext_lazy as _


class ProductFilter(django_filters.FilterSet):
    brand_filter = CharFilter(field_name='description', lookup_expr='icontains', label='Brand')
    price = RangeFilter(label='Price range')

    class Meta:
        model = Product
        fields = ['price']
