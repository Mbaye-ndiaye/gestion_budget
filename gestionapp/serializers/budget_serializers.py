from ..models.auth_models import CustomUser
from ..models.transaction_models import Transaction
from ..models.budget_models import Budget
from rest_framework import serializers
from ..serializers.auth_serializers import RegistrationSerializer

class BudgetSerialzer(serializers.ModelSerializer):
    user = RegistrationSerializer(read_only=True)

    class Meta:
        model = Budget
        fields = ['id', 'user', 'total_amount']