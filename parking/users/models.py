# models.py

from django.contrib.auth.models import AbstractUser, PermissionsMixin, Permission
from django.db import models

class User(AbstractUser, PermissionsMixin):
    # Add any additional fields you need
    groups = models.ManyToManyField(
        'Group', related_name='custom_user_set', blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Add a related_name to avoid the clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=False)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Group(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='custom_group_set', blank=True)