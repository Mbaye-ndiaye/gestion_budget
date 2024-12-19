
from django.apps import AppConfig

class GestionappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gestionapp'

    def ready(self):
        import gestionapp.signals  # Import des signaux ici

