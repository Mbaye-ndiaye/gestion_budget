from django.db import models
from ..models.auth_models import CustomUser



class Budget(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='budget')
    total_amount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f'budegt de {self.user.first_name} : {self.total_amount}'