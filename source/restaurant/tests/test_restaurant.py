from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Restaurant


class RestaurantAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.restaurant1 = Restaurant.objects.create(
            date="2023-05-01",
            restaurant="Ristorante Uno",
            planned_hours=10,
            hours_variance=2.5,
            actual_hours=12,
            budget=1000.0,
            sells=1200.0,
            budget_variance=200.0
        )
        self.restaurant2 = Restaurant.objects.create(
            date="2023-05-02",
            restaurant="Ristorante Due",
            planned_hours=8,
            hours_variance=1.0,
            actual_hours=9,
            budget=800.0,
            sells=950.0,
            budget_variance=150.0
        )

    def test_get_restaurants(self):
        url = reverse('restaurant_api:restaurant_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_restaurants_by_name(self):
        url = reverse('restaurant_api:restaurant_list')
        response = self.client.get(url, {'restaurant': 'Ristorante Uno'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['restaurant'], 'Ristorante Uno')

    def test_group_by_date_and_restaurant(self):
        url = reverse('restaurant_api:restaurant_list_aggregate')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for restaurant in response.data:
            if restaurant['restaurant'] == 'Ristorante Uno':
                self.assertEqual(restaurant['total_planned_hours'], 10)
                self.assertEqual(restaurant['total_hours_variance'], 2.5)
                self.assertEqual(restaurant['total_actual_hours'], 12)
                self.assertEqual(restaurant['total_budget'], 1000.0)
                self.assertEqual(restaurant['total_sells'], 1200.0)
                self.assertEqual(restaurant['total_budget_variance'], 200.0)
            elif restaurant['restaurant'] == 'Ristorante Due':
                self.assertEqual(restaurant['total_planned_hours'], 8)
                self.assertEqual(restaurant['total_hours_variance'], 1.0)
                self.assertEqual(restaurant['total_actual_hours'], 9)
                self.assertEqual(restaurant['total_budget'], 800.0)
                self.assertEqual(restaurant['total_sells'], 950.0)
                self.assertEqual(restaurant['total_budget_variance'], 150.0)
