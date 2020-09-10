from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Vehicle(models.Model):
    owner = models.CharField(max_length=200, db_index=True)
    make = models.CharField(max_length=200, db_index=True)
    model = models.SlugField(max_length=200, db_index=True)
    vin_number = models.CharField(max_length=200, db_index=True)
    purchase_date = models.DateTimeField(auto_now_add=False)
    last_service = models.DateTimeField(auto_now_add=False)
    description = models.TextField(blank=True)


    class Meta:
        ordering = ('make',)
        index_together = (('model'),)
    def __str__(self):
        return self.make

    def get_absolute_url(self):
        return reverse('vehicle_detail', args=[str(self.id)])