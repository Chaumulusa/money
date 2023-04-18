from django.urls import path
from . import views

urlpatterns = [
    path('book_car/<slug:slug>/', views.book_car, name='book'),
    path('book-room/<slug:slug>/', views.book_room, name='book-room'),
]
