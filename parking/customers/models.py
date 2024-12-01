from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    id = models.AutoField(primary_key=True)
    vehicle_number = models.CharField(max_length=20)
    registration_date = models.DateField(null=True, blank=True)
    is_regular_customer = models.BooleanField(default=False)
    contact_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        """
        Returns a string representation of the customer.

        :return: A string representation of the customer.
        :rtype: str
        """
        return self.vehicle_number

class RegularPass(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    start_date = models.DateField()
    duration_in_days = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        """
        Returns a string representation of the regular pass.

        :return: A string representation of the regular pass.
        :rtype: str
        """
        return f"Pass for {self.customer.vehicle_number} starting on {self.start_date}"