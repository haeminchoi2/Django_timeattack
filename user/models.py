from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
    phone = models.CharField(max_length=14, blank=True)
    address = models.CharField(max_length=60, blank=True)