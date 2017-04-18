from django.contrib.auth.models import User
from rest_framework import viewsets

from ..models import Calculator
from .serializers import UserSerializer, CalculatorSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides the list of Users and their details, without ability to change
    data or add new Users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CalculatorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Calculator.objects.all()
    serializer_class = CalculatorSerializer
