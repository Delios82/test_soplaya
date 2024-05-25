from django.urls import path
from .apis import *

app_name = 'restaurant'

urlpatterns = [
    path('list/', RestaurantList.as_view(), name='restaurant_list'),
    path('aggregate/', RestaurantAggregateList.as_view(), name='restaurant_list_aggregate'),
]
