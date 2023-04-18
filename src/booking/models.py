from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


from services.models import Car, Appartment


class CarHiring(models.Model):
    client_name = models.CharField(max_length=100)
    driving_licence_no = models.CharField(max_length=18)
    phone_number = models.CharField(max_length=18)
    vehicle = models.ForeignKey(Car, related_name='bookings', on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=200)
    pickup_date = models.CharField(blank=True, null=False, max_length=18)
    dropoff_date = models.CharField(blank=True, null=False, max_length=18)
    pickup_time = models.TimeField(auto_now=False)
    booked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-booked_at',)

    def __str__(self):
        return self.client_name
    

class RoomBooking(models.Model):
    client_name = models.CharField(max_length=100)
    gov_id = models.CharField(max_length=18)
    phone_number = models.CharField(max_length=18)
    room = models.ForeignKey(Appartment, related_name='bookings', on_delete=models.CASCADE)
    checkin_date = models.CharField(blank=True, null=False, max_length=18)
    checkout_date = models.CharField(blank=True, null=False, max_length=18)
    booked_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-booked_at',)

    def __str__(self):
        return self.client_name
    