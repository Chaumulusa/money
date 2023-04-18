from django.contrib import admin

from . import models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'passenger_capacity', 'cost_per_day', 'late_fee_per_hour']
    prepopulated_fields = {"slug": ("category_name",)} 
    list_filter = ['passenger_capacity', 'cost_per_day']


class CarAdmin(admin.ModelAdmin):
    list_display = ['brand_name', 'registration_number',
                    'transmission', 'availability']
    prepopulated_fields = {"slug": ("registration_number",)} 
    list_filter = ['model_year',]
    list_display_links = ['brand_name',]


class AppartmentCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', ]
    prepopulated_fields = {"slug": ("category_name",)} 
    list_filter = []
    list_display_links = ['category_name',]

class AppartmentAdmin(admin.ModelAdmin):
    list_display = ['category', 'appartment_name', 'bed_type', 'appartment_capacity', 'cost_per_night']
    prepopulated_fields = {"slug": ("category", "appartment_name",)} 
    list_filter = ['appartment_name','appartment_capacity', 'cost_per_night']
    list_display_links = ['appartment_name',]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name',]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Car, CarAdmin)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.ApartmentCategory, AppartmentCategoryAdmin)
admin.site.register(models.Appartment, AppartmentAdmin)