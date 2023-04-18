from django import forms
from .models import Service, Car, Appartment



class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'