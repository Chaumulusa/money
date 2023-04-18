from django.contrib import admin

from . import models


class CarHiringAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'driving_licence_no', 'phone_number', 'vehicle', 
                    'pickup_location', 'pickup_date', 'dropoff_date', 'pickup_time', 'booked_at']
    list_filter = ['booked_at', 'client_name']
    list_display_links = ['client_name', 'vehicle']

class RoomBookingAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'gov_id', 'phone_number', 'room', 'checkin_date', 'checkout_date', 'booked_at']
    list_filter = ['booked_at', 'client_name']
    list_display_links = ['client_name', 'room']


admin.site.register(models.CarHiring, CarHiringAdmin)
admin.site.register(models.RoomBooking, RoomBookingAdmin)