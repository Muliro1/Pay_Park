from django.contrib import admin
from .models import  ParkingSlot, Floor, Block, ParkingLot

admin.site.register(ParkingSlot)
admin.site.register(Floor)
admin.site.register(Block)
admin.site.register(ParkingLot)
