from django_filters import rest_framework as filters
from .models import AutoParkModel


class AutoParkFilters(filters.FilterSet):
    cars_year_lt = filters.NumberFilter(field_name='cars__year', lookup_expr='lt')

    class Meta:
        model = AutoParkModel
        fields = ('cars_year_lt',)
