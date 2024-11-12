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

class Floor(models.Model):
    id = models.AutoField(primary_key=True)
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='floors')
    floor_number = models.IntegerField()
    max_height_in_inch = models.IntegerField()
    number_of_wings = models.IntegerField()
    number_of_slots = models.IntegerField()
    is_covered = models.BooleanField(default=False)
    is_accessible = models.BooleanField(default=True)
    is_floor_full = models.BooleanField(default=False)
    is_reserved_reg_cust = models.BooleanField(default=False)

    def __str__(self):
        return f"Floor {self.floor_number} in Block {self.block.block_code}"

class ParkingSlot(models.Model):
    id = models.AutoField(primary_key=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='parking_slots')
    slot_number = models.IntegerField()
    is_occupied = models.BooleanField(default=False)
    is_reserved = models.BooleanField(default=False)
    is_handicapped_accessible = models.BooleanField(default=False)
    vehicle_type = models.CharField(max_length=50)

    def __str__(self):
        return f"Slot {self.slot_number} on Floor {self.floor.floor_number} in Block {self.floor.block.block_code}"