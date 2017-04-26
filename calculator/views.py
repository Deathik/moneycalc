from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.db import models

from .models import Calculator, BudgetExpenses, BudgetIncome
from .forms import ExpensesForm, IncomeForm


@login_required
def budget_edit(request):
    calc = Calculator.objects.select_related().get_or_create(user_id=request.user.pk)[0]
    total_inc = calc.budgetincome_set.all().aggregate(models.Sum(models.F('value')))['value__sum']
    total_exp = calc.budgetexpenses_set.all().aggregate(models.Sum(models.F('value')))['value__sum']
    if request.method == 'POST':
        inc_form = IncomeForm(request.POST)
        exp_form = ExpensesForm(request.POST)
        try:
            if inc_form.is_valid():
                value = inc_form.cleaned_data.get('value')
                changes = BudgetIncome(
                    calculator=calc,
                    value=value,
                    category=inc_form.cleaned_data.get('category'),
                )
                calc.inc_budget(value)
                changes.save()
                calc.save()
                return HttpResponseRedirect(reverse('calculator:budget_edit'))
            if exp_form.is_valid():
                value = exp_form.cleaned_data.get('value')
                changes = BudgetExpenses(
                    calculator=calc,
                    value=value,
                    category=exp_form.cleaned_data.get('category'),
                )
                calc.dec_budget(value)
                changes.save()
                calc.save()
                return HttpResponseRedirect(reverse('calculator:budget_edit'))
        except ValidationError:
            messages.add_message(request,
                                 messages.ERROR,
                                 "Value can't be negative or zero"
                                 )
    else:
        inc_form = IncomeForm()
        exp_form = ExpensesForm()

    return render(request, 'calculator/index.html', {
        'inc_form': inc_form,
        'exp_form': exp_form,
        'budget': total_inc - total_exp,
        'expenses': calc.budgetexpenses_set.all()[:5],
        'income': calc.budgetincome_set.all()[:5],
        'total_inc': total_inc,
        'total_exp': total_exp,
        })


@method_decorator(login_required, name='dispatch')
class IncomeList(generic.ListView):
    model = BudgetIncome

    def get_queryset(self):
        return Calculator.objects.get(pk=self.request.user.pk).budgetincome_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_inc = Calculator.objects.get(pk=self.request.user.pk).budgetincome_set.all()
        total_inc = total_inc.aggregate(total=models.Sum(models.F('value')))
        context['total_inc'] = total_inc['total']
        return context


@method_decorator(login_required, name='dispatch')
class ExpensesList(generic.ListView):
    model = BudgetExpenses

    def get_queryset(self):
        return Calculator.objects.get(pk=self.request.user.pk).budgetexpenses_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_exp = Calculator.objects.get(pk=self.request.user.pk).budgetexpenses_set.all()
        total_exp = total_exp.aggregate(total=models.Sum(models.F('value')))
        context['total_exp'] = total_exp['total']
        return context


@method_decorator(login_required, name='dispatch')
class IncomeDetailView(generic.DetailView):
    model = BudgetIncome

    def get_object(self, queryset=None):
        obj = get_object_or_404(
            Calculator.objects.get(user_id=self.request.user.pk).budgetincome_set, pk=self.kwargs['pk']
        )
        return obj


@method_decorator(login_required, name='dispatch')
class ExpensesDetailView(generic.DetailView):
    model = BudgetExpenses

    def get_object(self, queryset=None):
        obj = get_object_or_404(Calculator.objects.get(user_id=self.request.user.pk).budgetexpenses_set,
                                pk=self.kwargs['pk']
                                )
        return obj


@method_decorator(login_required, name='dispatch')
class IncomeYearView(generic.YearArchiveView):
    model = BudgetIncome
    date_field = 'date'
    make_object_list = True

    def get_queryset(self):
        return BudgetIncome.objects.filter(calculator__user=self.request.user)


@method_decorator(login_required, name='dispatch')
class IncomeMonthView(generic.MonthArchiveView):
    model = BudgetIncome
    date_field = 'date'

    def get_queryset(self):
        return BudgetIncome.objects.filter(calculator__user=self.request.user)
