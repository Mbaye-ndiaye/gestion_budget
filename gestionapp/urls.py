from django.urls import path
from .views import (RegistrationView, LoginView, LogoutView, AddTransactionView, ListTransactionsView, BudgetView, BudgetInitialView)

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  # à décommenter lorsque la connexion avec JWT sera utilisée
    path('transactions/', AddTransactionView.as_view(), name='add_transaction'),
    path('transactions/<int:user_id>/', ListTransactionsView.as_view(), name='list_transactions'),
    path('budget/<int:user_id>/', BudgetView.as_view(), name='get_budget'),
    path('budget/initial/', BudgetInitialView.as_view(), name='set_budget'),
]
