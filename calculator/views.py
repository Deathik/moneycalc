from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView, ListView

from .models import Calculator, BudgetExpenses, BudgetIncome
from .forms import ExpensesForm, IncomeForm


@login_required
def budget_edit(request):
    calc = Calculator.objects.get_or_create(user_id=request.user.pk)[0]
    expenses = BudgetExpenses.objects.filter(calculator=calc)[:5]
    income = BudgetIncome.objects.filter(calculator=calc)[:5]
    inc_form = IncomeForm()
    exp_form = ExpensesForm()
    return render(request, 'calculator/index.html', {
        'inc_form': inc_form,
        'exp_form': exp_form,
        'budget': calc.budget,
        'expenses': expenses,
        'income': income,
        'total_exp': calc.total_exp,
        'total_inc': calc.total_inc,
        })


def add_budget(request):
    if request.method == 'POST':
        calc = Calculator.objects.get_or_create(user_id=request.user.pk)[0]
        inc_form = IncomeForm(request.POST)
        if inc_form.is_valid():
            value = inc_form.cleaned_data.get('value')
            changes = BudgetIncome(
                calculator=calc,
                value=value,
                category=inc_form.cleaned_data.get('category'),
                )
            changes.save()
            calc.inc_budget(value)
            calc.save()
            return HttpResponseRedirect(reverse('calculator:budget_edit'))
    else:
        HttpResponseRedirect(reverse('calculator:budget_edit'))
    return HttpResponseRedirect(reverse('calculator:budget_edit'))


def del_budget(request):
    if request.method == 'POST':
        calc = Calculator.objects.get_or_create(user_id=request.user.pk)[0]
        exp_form = ExpensesForm(request.POST)
        if exp_form.is_valid():
            value = exp_form.cleaned_data.get('value')
            changes = BudgetExpenses(
                calculator=calc,
                value=value,
                category=exp_form.cleaned_data.get('category'),)
            changes.save()
            calc.dec_budget(value)
            calc.save()
            return HttpResponseRedirect(reverse('calculator:budget_edit'))
    else:
        HttpResponseRedirect(reverse('calculator:budget_edit'))
    return HttpResponseRedirect(reverse('calculator:budget_edit'))


class AllIncomeList(ListView):
    model = BudgetIncome
    total_inc = 0

    def get_queryset(self):
        self.total_inc = Calculator.objects.get(pk=self.request.user.pk).total_inc
        return Calculator.objects.get(pk=self.request.user.pk).budgetincome_set.all()


class AllExpensesList(ListView):
    model = BudgetExpenses
    total_exp = 0

    def get_queryset(self):
        self.total_exp = Calculator.objects.get(pk=self.request.user.pk).total_exp
        return Calculator.objects.get(pk=self.request.user.pk).budgetexpenses_set.all()