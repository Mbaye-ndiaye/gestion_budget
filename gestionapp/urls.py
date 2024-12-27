from django.urls import path
from .views import RegistrationView, LoginView, AddTransactionView, ListTransactionsView, BudgetView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('transactions/', AddTransactionView.as_view(), name='add_transaction'),
    path('transactions/<int:user_id>/', ListTransactionsView.as_view(), name='list_transactions'),
    path('budget/<int:user_id>/', BudgetView.as_view(), name='get_budget')
    
]
