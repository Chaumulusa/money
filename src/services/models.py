from tabnanny import verbose
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User

# from .utils import slugify_instance_title

from django.core.files import File
from io import BytesIO
from PIL import Image


class Category(models.Model):
    category_name = models.CharField(max_length=25)
    passenger_capacity = models.IntegerField()
    laggage = models.CharField(max_length=100, null=True, blank=True)
    fuel_type = models.CharField(max_length=20, choices=(('p', 'Petro'), ('d', 'Diesel')), default='Petro')
    cost_per_day = models.DecimalField(max_digits=9, decimal_places=2)
    late_fee_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    slug = models.SlugField(max_length=50, unique=True)
    
    class Meta:
        verbose_name_plural = 'Car Categories'
    
    def __str__(self):
        return self.category_name


class Location(models.Model):
    location_name = models.CharField(max_length=25)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    province = models.CharField(max_length=50)

    def __str__(self):
        return self.location_name
    

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="Media/Services/Service-Thumbnails")
    slug = models.SlugField(blank=True, null=True, unique=True)
    


class Car(models.Model):
    category = models.ForeignKey(Category, related_name='cars', on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=100, null=True, blank=True)
    registration_number = models.CharField(max_length=15)
    model_name = models.CharField(max_length=50)
    model_year = models.IntegerField()
    # mileage_count = models.IntegerField()
    transmission = models.CharField(choices=(('man', 'Manual'), ('auto', 'Automatic')), max_length=15)
    availability = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to='services/uploads', blank=True, null=True)
    image_thumbnail = models.ImageField(upload_to='services/uploads', blank=True, null=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-registered_at',)
    
    def __str__(self):
        return self.model_name

    def get_image_thumbnail(self):
        if self.image_thumbnail:
            return self.image_thumbnail
        else:
            if self.thumbnail:
                self.image_thumbnail = self.make_image_thumbnail(self.thumbnail)
                self.save()

                return self.image_thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240x.jpg'

    def make_image_thumbnail(self, thumbnail, size=(300, 300)):
        img = Image.open(thumbnail)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        name = thumbnail.name.replace('services/uploads/', '')
        image_thumbnail = File(thumb_io, name=name)

        return image_thumbnail


class ApartmentCategory(models.Model):
    category_name = models.CharField(max_length=80, choices=(('spe', 'Special'), ('reg', 'Regular'), ('vip', 'VIP')), default='VIP')
    # checking_out_time = models.TimeField(auto_now_add=False)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Appartment Categories'
    
    def __str__(self):
        return self.category_name


class Appartment(models.Model):
    category = models.ForeignKey(ApartmentCategory, related_name='rooms', on_delete=models.CASCADE)
    appartment_name = models.CharField(max_length=200)
    bed_type = models.CharField(max_length=20, choices=(('sin', 'Single'), ('dou', 'Double'), ('que', 'Queen'), ('kin', 'King')), default='Single')
    appartment_capacity = models.IntegerField()
    cost_per_night = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to="Services/appartments-thumbnails/")
    picture1 = models.ImageField(upload_to="Services/appartments-thumbnails/", blank=True, null=True)
    picture2 = models.ImageField(upload_to="Services/appartments-thumbnails/", blank=True, null=True)
    picture3 = models.ImageField(upload_to="Services/appartments-thumbnails/", blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    availability = models.BooleanField(default=True)
    status = models.CharField(max_length=20, choices=(('booked', 'Booked'), ('available', 'Available')), default='Available')

    def __str__(self):
        return self.appartment_name
    