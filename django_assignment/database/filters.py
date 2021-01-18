import django_filters
from django_filters import DateFilter

from .models import *

class SampleFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='time', lookup_expr='gte')
    end_date = DateFilter(field_name='time', lookup_expr='lte')
    class Meta:
        model = Sample
        fields = '__all__'
        exclude = ['time']