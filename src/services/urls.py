from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_list, name='cars'),
    path('services/', views.service_list_view, name='services'),
    path('appartments/', views.appartment_list_view, name='appartments'),
    path('cars/<slug:slug>/', views.car_detail, name='car-detail'),
    path('rooms/<slug:slug>/', views.room_detail, name='room-detail')
]