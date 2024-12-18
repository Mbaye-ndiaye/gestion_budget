from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import CustomUser, Budget, Transaction
from ..serializers import RegistrationSerializer, BudgetSerialzer, TransactionSerializer

class AddTransactionView(APIView):
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            transaction = serializer.save()  # Sauvegarde la transaction si elle est valide
            return Response({
                "message": "Transaction ajoutée avec succès",
                "Budget_total": transaction.budget.total_amount  # Accède à la valeur du budget
            }, status=status.HTTP_201_CREATED)  # Utilisez le code de statut 201 pour création
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Si la sérialisation échoue, renvoie les erreurs


class ListTransactionsView(APIView):
    def get(self, request, user_id):
        user = CustomUser.objects.get(id=user_id)
        serializer = BudgetSerialzer(user.budget)
        return Response(serializer.data, status.HTTP_200_OK)