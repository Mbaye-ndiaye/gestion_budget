from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Manager personnalisé pour CustomUser
class CustomUserManager(BaseUserManager):
    """
    Gestionnaire personnalisé pour CustomUser.
    """
    def create_user(self, username, email, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError("L'adresse e-mail doit être renseignée.")
        if not phone_number:
            raise ValueError("Le numéro de téléphone doit être renseigné.")
        if not username:
            raise ValueError("Le nom d'utilisateur doit être renseigné.")

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)  # Hache le mot de passe
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone_number, password=None, **extra_fields):
        """
        Création de superutilisateur avec is_staff et is_superuser définis à True.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, phone_number, password, **extra_fields)

# Modèle utilisateur personnalisé
class CustomUser(AbstractUser):
    """
    Modèle utilisateur personnalisé basé sur AbstractUser.
    """
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['email', 'phone_number', 'first_name', 'last_name']  # Champs obligatoires lors de la création d'utilisateur
    USERNAME_FIELD = 'username'  # Le champ utilisé pour l'authentification

    objects = CustomUserManager()  # Associe le gestionnaire personnalisé

    def __str__(self):
        return self.username
