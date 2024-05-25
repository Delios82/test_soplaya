from django_filters import FilterSet, CharFilter
from restaurant.models import Restaurant


class RestaurantFilter(FilterSet):
    class Meta:
        model = Restaurant
        fields = {
            'restaurant': ['exact'],
            'date': ['exact', 'gte', 'lte'],
        }
