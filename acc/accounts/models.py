from django.db import models

# accounts/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='customuser_set') 
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions_set')

