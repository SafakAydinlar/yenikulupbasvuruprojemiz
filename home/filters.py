import django_filters

from .models import *

class FilterFunction(django_filters.FilterSet):
    class Meta:
        model = Basvuru
        fields = ['name','surname', 'posta']


        