from django import forms

from .models import BudgetExpenses, BudgetIncome


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = BudgetExpenses
        exclude = ['calculator', 'date', 'total']


class IncomeForm(forms.ModelForm):
    class Meta:
        model = BudgetIncome
        exclude = ['calculator', 'date', 'total']
