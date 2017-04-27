from django import forms

from .models import BudgetExpenses, BudgetIncome
from .validators import more_than_zero_validator


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = BudgetExpenses
        fields = ('value', 'category')


class IncomeForm(forms.ModelForm):
    class Meta:
        model = BudgetIncome
        fields = ('value', 'category')