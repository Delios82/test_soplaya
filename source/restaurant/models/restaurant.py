from django.contrib.gis.db import models


class Restaurant(models.Model):
    date = models.DateField("date", max_length=255, null=False)
    restaurant = models.CharField("restaurant", null=False, max_length=255)
    planned_hours = models.IntegerField("planned hours", default=0)
    hours_variance = models.FloatField("hours variance", default=0)
    actual_hours = models.IntegerField("actual hours", default=0)
    budget = models.FloatField("budget", default=0)
    sells = models.FloatField("sells", default=0)
    budget_variance = models.FloatField("budget variance", default=0)

    class Meta:
        app_label = 'restaurant'
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'

    def __str__(self):
        return self.restaurant
