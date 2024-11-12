from django.db import models

class ParkingLot(models.Model):
    id = models.AutoField(primary_key=True)
    number_of_blocks = models.IntegerField()
    is_slot_available = models.BooleanField(default=True)
    address = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
    is_reentry_allowed = models.BooleanField(default=False)
    operating_company = models.CharField(max_length=255)
    is_valet_parking_available = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.address} - {self.operating_company}"

class Block(models.Model):
    id = models.AutoField(primary_key=True)
    parking_lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE, related_name='blocks')
    block_code = models.CharField(max_length=10)
    number_of_floors = models.IntegerField()
    is_block_full = models.BooleanField(default=False)

    def __str__(self):
        return f"Block {self.block_code} in {self.parking_lot.address}"