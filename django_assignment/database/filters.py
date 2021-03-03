import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class SampleFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='time', lookup_expr='gte')
    end_date = DateFilter(field_name='time', lookup_expr='lte')
    sample_name = CharFilter(field_name='sample_name', lookup_expr='icontains')
    description = CharFilter(field_name='description', lookup_expr='icontains')
    
    class Meta:
        model = Sample
        fields = '__all__'
        exclude = ['time']