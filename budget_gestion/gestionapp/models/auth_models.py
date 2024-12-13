from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Email obligatoire et unique
    phone_number = models.CharField(max_length=15, unique=True)  # Numéro de téléphone
    first_name = models.CharField(max_length=50)  # Prénom
    last_name = models.CharField(max_length=50)   # Nom

    REQUIRED_FIELDS = ['email', 'phone_number', 'first_name', 'last_name']  # Champs obligatoires
    USERNAME_FIELD = 'username'  # Identifiant unique pour l'authentification
