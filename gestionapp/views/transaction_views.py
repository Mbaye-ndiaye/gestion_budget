from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import CustomUser, Budget, Transaction
from ..serializers import RegistrationSerializer, BudgetSerialzer, TransactionSerializer
from rest_framework.exceptions import NotFound

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


# class ListTransactionsView(APIView):
#     def get(self, request, user_id):
#         user = CustomUser.objects.get(id=user_id)
#         serializer = BudgetSerialzer(user.budget)
#         return Response(serializer.data, status.HTTP_200_OK)
    
class ListTransactionsView(APIView):
    def get(self, request, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise NotFound("Utilisateur non trouvé")

        # Récupérer toutes les transactions liées au budget de l'utilisateur
        transactions = Transaction.objects.filter(budget=user.budget)
        serializer = TransactionSerializer(transactions, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)