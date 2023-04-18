from django.contrib import admin
from django.contrib.auth.models import Group

from .models import CustomerReview, About, Contact, Visitor


admin.site.register(CustomerReview)
admin.site.unregister(Group)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Visitor)