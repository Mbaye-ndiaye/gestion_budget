from rest_framework import serializers
from ..models.budgetIinitial_model import BudgetInitial

class BudgetInitialSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetInitial
        fields = ['id', 'user', 'montant', 'updated_at']
        read_only_fields = ['id', 'user', 'updated_at']
