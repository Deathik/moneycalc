from rest_framework import serializers
from django.contrib.auth.models import User

from ..models import Calculator, BudgetIncome, BudgetExpenses


class UserSerializer(serializers.HyperlinkedModelSerializer):
    calculator = serializers.HyperlinkedRelatedField(many=False,
                                                     view_name='calculator-detail',
                                                     read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'calculator')


class CalculatorSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Calculator
        fields = ('url', 'user', 'id', 'budget')
