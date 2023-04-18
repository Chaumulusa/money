from django.shortcuts import render, get_object_or_404, redirect
from services.models import Category, Car, Service, ApartmentCategory, Appartment
from django.utils.text import slugify


def car_list(request):
    template = 'car-list.html'
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, template, context)


def car_detail(request, slug):
    try:
        car = Car.objects.get(slug=slug)
        related_cars = Car.objects.all().filter(category=car.category)
        template = 'car-single.html'
        context = {'car': car, 'related_cars': related_cars}
    except Car.DoesNotExist:
        return redirect('page-not-found')
    
    return render(request, template, context)


def service_list_view(request):
    services = Service.objects.all()

    context = { 'services': services }
    template = 'services.html'
    return render(request, template, context)


def appartment_list_view(request):
    template = 'appartments.html'

    appartments = Appartment.objects.all()
    vip_appartments = Appartment.objects.all().filter(category__category_name='vip')
    special_appartments = Appartment.objects.all().filter(category__category_name='spe')
    regular_appartments = Appartment.objects.all().filter(category__category_name='reg')
    context = {
        'appartments': appartments,
        'special_appartments': special_appartments,
        'vip_appartments': vip_appartments,
        'regular_appartments': regular_appartments
        }
    return render(request, template, context)


def room_detail(request, slug):
    try:
        room = Appartment.objects.get(slug=slug)
        template = 'room-detail.html'
        context = {'room': room,}
    except Appartment.DoesNotExist:

        return redirect('page-not-found')
    
    return render(request, template, context)



def add_service(request):
    if request.method == "POST":
        service = Service()
        service.name = request.POST.get('name')
        service.description = request.POST.get('description')