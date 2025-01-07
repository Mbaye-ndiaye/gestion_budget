from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from ..models.budget_models import Budget
from ..serializers.budgetInitial_serializer import BudgetInitialSerializer


class BudgetInitialView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        budget_value = request.data.get('montant')

        # Vérifier si le montant est fourni
        if not budget_value:
            return Response(
                {"error": "Le montant du budget est requis."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            budget_value = float(budget_value)
            if budget_value <= 0:
                return Response(
                    {"error": "Le montant doit être supérieur à zéro."}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
        except ValueError:
            return Response(
                {"error": "Le montant doit être un nombre valide."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # Vérifier si l'utilisateur a déjà un budget initial
        budget_initial, created = Budget.objects.get_or_create(user=user)

        # Mettre à jour le budget initial
        budget_initial.montant = budget_value
        budget_initial.save()

        # Vérifier si l'utilisateur a déjà un budget
        budget, budget_created = Budget.objects.get_or_create(user=user)

        # Mettre à jour le budget avec le montant du budget initial
        budget.total_amount = budget_value
        budget.save()

        # Retourner la réponse avec les détails du budget
        serializer = BudgetInitialSerializer(budget_initial)
        return Response(
            {"message": "Budget initial défini et ajouté au budget total avec succès.", "budget_initial": serializer.data}, 
            status=status.HTTP_200_OK
        )
