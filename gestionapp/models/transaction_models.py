from django.db import models
from ..models.budget_models import Budget
from decimal import Decimal

class Transaction(models.Model):
    TYPE_CHOICES = [
        (
            'depense', 'Depense'),
            ('revenu', 'Revenu')
        
    ]

    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='transations')
    date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    montant = models.DecimalField(max_digits=13, decimal_places=2)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if self.transaction_type == 'depense':
            # Verifeir que le budget restant est >= 40% du total
            # if self.budget.total_amount - self.montant < self.budget.total_amount * 0.4:
            if self.budget.total_amount - self.montant < Decimal('0.4') * self.budget.total_amount:
                raise ValueError("Le budget restant doit etre egal ou superieur a 40% du budget total")
            self.budget.total_amount -= self.montant
        elif self.transaction_type == 'revenu':
            self.budget.total_amount += self.montant
        self.budget.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.transaction_type} de {self.montant} - {self.date}"