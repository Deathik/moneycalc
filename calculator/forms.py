from django import forms

from .models import BudgetExpenses, BudgetIncome


class CalculatorForm(forms.Form):
        add_to_budget = forms.DecimalField(
            max_digits=12,
            decimal_places=2,
            required=False)
        delete_from_budget = forms.DecimalField(
            max_digits=12,
            decimal_places=2,
            required=False)


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = BudgetExpenses
        exclude = ['calculator', 'date']


class IncomeForm(forms.ModelForm):
    class Meta:
        model = BudgetIncome
        exclude = ['calculator', 'date']
