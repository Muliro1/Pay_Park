from django.contrib import admin
from .models import Customer, RegularPass

# Register your models here.
admin.site.register(Customer)
admin.site.register(RegularPass)