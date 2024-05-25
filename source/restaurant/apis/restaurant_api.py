from rest_framework.generics import ListCreateAPIView, GenericAPIView, ListAPIView
from restaurant.models import Restaurant
from rest_framework.response import Response
from restaurant.serializers import RestaurantSerializer
from restaurant.filters import RestaurantFilter
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend


class RestaurantList(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RestaurantFilter
    ordering_fields = '__all__'


class RestaurantAggregateList(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RestaurantFilter

    def get_queryset(self):
        queryset = Restaurant.objects.all()
        queryset = queryset.annotate(
            total_planned_hours=Sum('planned_hours'),
            total_hours_variance=Sum('hours_variance'),
            total_actual_hours=Sum('actual_hours'),
            total_budget=Sum('budget'),
            total_sells=Sum('sells'),
            total_budget_variance=Sum('budget_variance')
        ).values('restaurant', 'date', 'total_planned_hours', 'total_hours_variance', 'total_actual_hours',
                 'total_budget', 'total_sells', 'total_budget_variance')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        return Response(queryset)
