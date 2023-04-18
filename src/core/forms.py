from django import forms
from . import models


class CustomerReviewForm(forms.ModelForm):
    class Meta:
        model = models.CustomerReview
        fields = ['name', 'occupation', 'comments']
        widgets = {
            'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name'
            }),
            'occupation': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Occupation'
            }),
            'comments': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Comments'
            }),
        }

