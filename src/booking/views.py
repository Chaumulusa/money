from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from .models import CarHiring, RoomBooking
from services.models import Category, Car, Appartment


def book_car(request, slug):
    car = Car.objects.get(slug=slug)
    related_cars = Car.objects.all().filter(category=car.category)

    
    if request.method == 'POST':
        booking = CarHiring()

        booking.client_name = request.POST.get('client_name')
        booking.driving_licence_no = request.POST.get('driving_licence_no')
        booking.phone_number = request.POST.get('phone_number')
        booking.vehicle = car
        booking.pickup_location = request.POST.get('pickup_location')
        booking.pickup_date = request.POST.get('pickup_date')
        booking.dropoff_date = request.POST.get('dropoff_date')
        booking.pickup_time = request.POST.get('pickup_time')
        booking.save()

        return redirect('car-success')

    return render(request, 'booking.html', {'car':car, 'related_cars': related_cars})


def book_room(request, slug):
    room = Appartment.objects.get(slug=slug)

    if request.method == "POST":
        booking = RoomBooking()
        booking.client_name = request.POST.get('client_name')
        booking.gov_id = request.POST.get('gov_id')
        booking.phone_number = request.POST.get('phone_number')
        booking.room = room
        booking.checkin_date = request.POST.get('checkin_date')
        booking.checkout_date = request.POST.get('checkout_date')
        booking.room.status = "booked"
        booking.save()
        
        return redirect('room-success')
    template = 'book-appartment.html'

    context = {}
    return render(request, template, context)