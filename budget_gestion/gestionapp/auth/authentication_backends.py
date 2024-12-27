from django.contrib.auth.backends import BaseBackend
from gestionapp.models import CustomUser

class PhoneNumberBackend(BaseBackend):
    """
    Backend d'authentification personnalisé pour se connecter avec le numéro de téléphone.
    """
    def authenticate(self, request, phone_number=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(phone_number=phone_number)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
