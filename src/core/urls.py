from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('site-admin/', views.admin, name='system-admin'),
    path('', views.home_view, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('car-hiring/<pk>/', views.car_hiring_detail, name='hiring-detail'),
    path('page-not-found/', views.four_or_four_page, name='page-not-found'),
    path('car-hire-success/', views.car_hire_success, name='car-success'),
    path('room-book-success/', views.room_success, name='room-success'),
    path('gen-pdf/<pk>', views.generate_pdf, name='gen-pdf'),
    path('gen-pdf/<pk>', views.generate_pdf_room, name='gen-pdf-room'),
    path('car-hirings/', views.car_hirings, name='hirings'),
    path('room-bookings/', views.room_bookings, name='bookings'),
    path('room-bookings/<pk>/', views.room_booking_detail, name='booking-detail'),

    path('logout/', views.logout_view, name='logout'),
    path('login/', views.admin_login, name='login'),
]