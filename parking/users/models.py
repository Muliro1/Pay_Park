from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.contrib.auth.models import User


class User(AbstractUser, PermissionsMixin):
    # Add any additional fields you nee
    groups = models.ManyToManyField(
        'Group',related_name='custom_user_set', blank=True
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
    users = models.ManyToManyField(User, related_name='custom_group_set', blank=True)

    def __str__(self):
        return self.name