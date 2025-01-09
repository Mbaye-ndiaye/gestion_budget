from rest_framework import serializers
from ..serializers.budget_serializers import BudgetSerialzer
from ..models.transaction_models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'budget', 'date', 'transaction_type', 'montant', 'description']
        read_only_fields = (True,)

        def create(self, validated_data):
            transaction = Transaction(**validated_data)
            budget = transaction.budget

            if transaction.transaction_type == 'depense':
                if budget.total_amount - transaction.montant < budget.total_amount * 0.4:
                    raise serializers.ValidationError("Le budget restant doit etre superieur ou egal a 40% du budget total.")
                budget.total_amount -= transaction.montant
            elif transaction.transaction_type == 'revenu':
                budget.total_amount += transaction.montant

            budget.save()
            transaction.save()
            return transaction