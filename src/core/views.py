from django.shortcuts import render, redirect
from services.models import Car, Category, Service
from .models import CustomerReview, About, Contact
from .forms import CustomerReviewForm
from booking.models import CarHiring, RoomBooking
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.core.cache import cache



def home_view(request):
    customer_reviews = CustomerReview.objects.all()
    home_display_cars = Car.objects.all()[: 8]
    car_count = Car.objects.all().count()
    customer_count = CustomerReview.objects.all().count()
    about = About.objects.all()
    services = Service.objects.all()[:4]
    visit_count = cache.get('site_visits', 0)

    if request.method == 'POST':
        review = CustomerReview()
        name = request.POST.get('name')
        occupation = request.POST.get('occupation')
        comments = request.POST.get('comments')
        review.name = name
        review.occupation = occupation
        review.comments = comments
        review.save()

        return redirect('home')
    context = {
        'home_display_cars': home_display_cars,
        'customer_reviews': customer_reviews,
        'car_count': car_count,
        'customer_count': customer_count,
        'about': about,
        'services': services,
        'visit_count': visit_count,
    }
    return render(request, 'index.html', context)


def about(request):
    about = About.objects.all()
    customer_reviews = CustomerReview.objects.all()
    car_count = Car.objects.all().count()
    customer_count = CustomerReview.objects.all().count()
    return render(request, 'about.html', { 'about':about, 'customer_reviews': customer_reviews, 'car_count': car_count, 'customer_count': customer_count })


def success(request):
    return render(request, 'success.html')


def car_hire_success(request):
    return render(request, 'car-success.html')


def room_success(request):
    return render(request, 'room-success.html')


def contact(request):

    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.subject = request.POST.get('subject')
        contact.message = request.POST.get('message')
        contact.save()

        return redirect('success')
    return render(request, 'contact.html', {})


def four_or_four_page(request):
    return render(request, '404/page-not-found.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('system-admin')
        else:
            # Return an 'invalid login' error message.
            return redirect('login')
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def admin(request):
    car_hirings = CarHiring.objects.all()[:5]
    room_bookings = RoomBooking.objects.all()[:5]
    context = {
        'car_hirings': car_hirings,
        'bookings': room_bookings,
    }
    return render(request, 'admin.html', context)


def car_hirings(request):
    car_hirings = CarHiring.objects.all()
    return render(request, 'hirings.html', {'car_hirings': car_hirings})


def car_hiring_detail(request, pk):

    hiring = CarHiring.objects.get(pk=pk)

    context = {'hiring':hiring}
    return render(request, 'hiring-detals.html', context)


def room_bookings(request):
    bookings = RoomBooking.objects.all()
    context = {'bookings':bookings}
    return render(request, 'room-bookings.html', context)


def room_booking_detail(request, pk):
    booking = RoomBooking.objects.get(pk=pk)
    return render(request, 'room-booking-detail.html', {'booking':booking})


def generate_pdf(request, pk):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 12)

    hiring = CarHiring.objects.get(pk=pk)

    lines = []
    lines.append(f"Client Name: {hiring.client_name}")
    lines.append(" ")
    lines.append(f"Client Driver's Licence: {hiring.driving_licence_no}")
    lines.append(" ")
    lines.append(f"Client Phone: {hiring.phone_number}")
    lines.append(" ")
    lines.append(f"Booked vehicle: {hiring.vehicle}")
    lines.append(" ")
    lines.append(f"Pickup Location: {hiring.pickup_location}")
    lines.append(" ")
    lines.append(f"Pickup Date: {hiring.pickup_date}")
    lines.append(" ")
    lines.append(f"Dropoff Date: {hiring.dropoff_date}")
    lines.append(" ")
    lines.append(f"Pick up time: {hiring.pickup_time}")
    lines.append(" ")
    lines.append(f"Booked at: {hiring.booked_at}")
    lines.append(" ")
    lines.append(f"Cost per day: K{hiring.vehicle.category.cost_per_day}")
    lines.append("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    for line in lines:
        textob.textLines(line)

    c.drawText(textob)
    c.setTitle("car-hire receipt")
    c.drawString(300, 20, "Car Hiring Receipt")
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='car-hirings.pdf')


def generate_pdf_room(request, pk):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 12)

    booking = RoomBooking.objects.get(pk=pk)

    lines = []
    lines.append(f"Client Name: {booking.client_name}")
    lines.append(" ")
    lines.append(f"Client Driver's Licence: {booking.gov_id}")
    lines.append(" ")
    lines.append(f"Client Phone: {booking.phone_number}")
    lines.append(" ")
    lines.append(f"Booked vehicle: {booking.room}")
    lines.append(" ")
    lines.append(f"Checkin Date: {booking.checkin_date}")
    lines.append(" ")
    lines.append(f"Checkout date: {booking.checkout_date}")
    lines.append(" ")
    lines.append(f"Booked at: {booking.booked_at}")
    lines.append(" ")
    lines.append(f"Cost per night: K{booking.room.category.cost_per_night}")
    lines.append("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

    for line in lines:
        textob.textLines(line)

    c.drawText(textob)
    c.setTitle("room-booking receipt")
    c.drawString(300, 30, "Room Booking Receipt")
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='room-booking-receipt.pdf')