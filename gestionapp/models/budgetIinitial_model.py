from django.db import models
from ..models.auth_models import CustomUser
from ..models.budget_models import Budget


class BudgetInitial(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    montant = models.FloatField(default=0.0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} - {self.montant}"
