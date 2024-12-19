from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Exemple d'action après la création d'un utilisateur
        print(f"Un utilisateur a été créé : {instance}")
