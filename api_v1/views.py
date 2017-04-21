from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from .permissons import IsOwner
from calculator.models import Calculator, BudgetIncome
from .serializers import UserSerializer, CalculatorSerializer, BudgetIncomeSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides the list of Users and their details, without ability to change
    data or add new Users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CalculatorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Calculator.objects.all()
    serializer_class = CalculatorSerializer
    permission_classes = (IsOwner, permissions.IsAuthenticated)

    def get_queryset(self):
        return Calculator.objects.filter(user=self.request.user)