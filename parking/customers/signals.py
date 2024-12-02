from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Customer
from django.utils import timezone

@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance, vehicle_number='', registration_date=timezone.now(), is_regular_customer=False, contact_number='')

@receiver(post_save, sender=User)
def save_customer(sender, instance, **kwargs):
    # Check if the user has a customer instance before saving
    if hasattr(instance, 'customer'):
        instance.customer.save()

