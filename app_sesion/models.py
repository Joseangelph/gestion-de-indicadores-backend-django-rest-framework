
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('administrador', 'Administrador'),
        ('experto', 'Experto'),
        ('cliente', 'Cliente'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)