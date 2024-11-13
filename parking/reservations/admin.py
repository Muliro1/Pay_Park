from django.contrib import admin
from .models import ParkingReservation, ParkingSlip

# Register your models here.

admin.site.register(ParkingReservation)
admin.site.register(ParkingSlip)
