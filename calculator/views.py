from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Calculator, BudgetExpenses, BudgetIncome
from .forms import CalculatorForm, ExpensesForm, IncomeForm


@login_required
def budget_edit(request):
    calc = Calculator.objects.get_or_create(user_id=request.user.pk)[0]
    expenses = BudgetExpenses.objects.filter(calculator=calc)[::-1]
    income = BudgetIncome.objects.filter(calculator=calc)[::-1]
    inc_form = IncomeForm()
    exp_form = ExpensesForm()
    return render(request, 'calculator/index.html', {
        'inc_form': inc_form,
        'exp_form': exp_form,
        'budget': calc.budget,
        'expenses': expenses,
        'income': income,
        })


def base(request):
    return render(request, 'base.html', {})


def add_budget(request):
    if request.method == 'POST':
        calc = Calculator.objects.get_or_create(user_id=request.user.pk)[0]
        inc_form = IncomeForm(request.POST)
        if inc_form.is_valid():
            value = inc_form.cleaned_data.get('value')
            changes = BudgetIncome(
                calculator=calc,
                value=value,
                category=inc_form.cleaned_data.get('category'),)
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
