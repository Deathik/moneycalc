from django import forms

from .models import BudgetExpenses, BudgetIncome
from .validators import more_than_zero_validator


class ExpensesForm(forms.ModelForm):

    class Meta:
        model = BudgetExpenses
        fields = ('value', 'category')

    def __init__(self, *args, **kwargs):
        super(ExpensesForm, self).__init__(*args, **kwargs)
        self.fields['value'].widget.attrs.update({'class' : 'form-control'})
        self.fields['category'].widget.attrs.update({'class' : 'form-control'})

class IncomeForm(forms.ModelForm):

    class Meta:
        model = BudgetIncome
        fields = ('value', 'category')

    def __init__(self, *args, **kwargs):
        super(IncomeForm, self).__init__(*args, **kwargs)
        self.fields['value'].widget.attrs.update({'class' : 'form-control'})
        self.fields['category'].widget.attrs.update({'class' : 'form-control'})