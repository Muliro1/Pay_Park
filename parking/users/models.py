from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

class User(AbstractUser, PermissionsMixin):
    # Add any additional fields you nee
    groups = models.ManyToManyField(
        'Group',related_name='user_set'
    )
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Group(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='groups')

    def __str__(self):
        return self.name