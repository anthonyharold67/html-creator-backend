import django_filters
from django_filters import DateFilter
from .models import HtmlCreatorModel

class HtmlCreatorFilter(django_filters.FilterSet):
    created_at = DateFilter(field_name='created_at', lookup_expr='date')  
    last_updated = DateFilter(field_name='last_updated', lookup_expr='date')  

    class Meta:
        model = HtmlCreatorModel
        fields = ['entity_id', 'created_at', 'last_updated']
