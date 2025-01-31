from django.db import models
from customers.models import Customer  # Import the Customer model
from parking.models import ParkingSlot  # Import the ParkingSlot model
from django.utils import timezone

# Create your models here.
class ParkingReservation(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_timestamp = models.DateTimeField()
    duration_in_minutes = models.IntegerField()
    booking_date = models.DateField()
    parking_slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a string representation of the reservation in the format
        "Reservation for <vehicle_number> on <start_timestamp>".

        :return: A string representation of the reservation.
        :rtype: str
        """
        return f"Reservation for {self.customer.vehicle_number} on {self.start_timestamp}"

class ParkingSlip(models.Model):
    id = models.AutoField(primary_key=True)
    reservation = models.ForeignKey(ParkingReservation, on_delete=models.CASCADE)
    issue_date = models.DateField(default=timezone.now)
    entry_time = models.DateTimeField(default=timezone.now)
    exit_time = models.DateTimeField(null=True, blank=True)
    total_amount = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)

    def __str__(self):
        """
        Returns a string representation of the parking slip in the format
        "Slip for reservation <reservation_id> issued on <issue_date>".

        :return: A string representation of the parking slip.
        :rtype: str
        """
        
        return f"Slip for reservation {self.reservation.id} issued on {self.issue_date}"

