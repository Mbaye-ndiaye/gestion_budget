# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from ..models import  CustomUser, Budget, Transaction
# from ..serializers import RegistrationSerializer, BudgetSerialzer, TransactionSerializer

# class BudgetView(APIView):
#     def get(self, request, user_id):
#         user = CustomUser.objects.get(id=user_id)
#         serializer = BudgetSerialzer(user.budget)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import CustomUser
from ..serializers import BudgetSerialzer

class BudgetView(APIView):
    def get(self, request, user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
            if not hasattr(user, 'budget'):
                return Response({"error": "Cet utilisateur n'a pas encore de budget."}, status=status.HTTP_404_NOT_FOUND)
            serializer = BudgetSerialzer(user.budget)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "Utilisateur introuvable."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
