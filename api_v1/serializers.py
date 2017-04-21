from rest_framework import serializers
from django.contrib.auth.models import User

from calculator.models import Calculator, BudgetIncome, BudgetExpenses


class UserSerializer(serializers.HyperlinkedModelSerializer):
    calculator = serializers.HyperlinkedRelatedField(many=False,
                                                     view_name='calculator-detail',
                                                     read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'calculator')


class BudgetIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetIncome
        fields = ('value', 'date', 'category')


class BudgetExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetExpenses
        fields = ('value', 'date', 'category')


class CalculatorSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    budgetincome_set = BudgetIncomeSerializer(many=True, read_only=True)
    budgetexpenses_set = BudgetExpensesSerializer(many=True, read_only=True)

    class Meta:
        model = Calculator
        fields = ('url', 'user', 'id', 'budget', 'total_inc', 'total_exp', 'budgetincome_set', 'budgetexpenses_set')


