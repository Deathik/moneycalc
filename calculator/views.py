from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, YearArchiveView, MonthArchiveView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Calculator, BudgetExpenses, BudgetIncome
from .forms import ExpensesForm, IncomeForm


@login_required
def budget_edit(request):
    calc = Calculator.objects.get_or_create(user_id=request.user.pk)[0]
    if request.method == 'POST':
        inc_form = IncomeForm(request.POST)
        exp_form = ExpensesForm(request.POST)
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
        if exp_form.is_valid():
            exp_form = ExpensesForm(request.POST)
            if exp_form.is_valid():
                value = exp_form.cleaned_data.get('value')
                changes = BudgetExpenses(
                    calculator=calc,
                    value=value,
                    category=exp_form.cleaned_data.get('category'),
                )
                changes.save()
                calc.dec_budget(value)
                calc.save()
                return HttpResponseRedirect(reverse('calculator:budget_edit'))
    else:
        inc_form = IncomeForm()
        exp_form = ExpensesForm()

    return render(request, 'calculator/index.html', {
        'inc_form': inc_form,
        'exp_form': exp_form,
        'budget': calc.budget,
        'expenses': calc.budgetexpenses_set.all()[:5],
        'income': calc.budgetincome_set.all()[:5],
        'total_exp': calc.total_exp,
        'total_inc': calc.total_inc,
        })


@method_decorator(login_required, name='dispatch')
class IncomeList(ListView):
    model = BudgetIncome
    total_inc = 0

    def get_queryset(self):
        self.total_inc = Calculator.objects.get(pk=self.request.user.pk).total_inc
        return Calculator.objects.get(pk=self.request.user.pk).budgetincome_set.all()


@method_decorator(login_required, name='dispatch')
class ExpensesList(ListView):
    model = BudgetExpenses
    total_exp = 0

    def get_queryset(self):
        self.total_exp = Calculator.objects.get(pk=self.request.user.pk).total_exp
        return Calculator.objects.get(pk=self.request.user.pk).budgetexpenses_set.all()


@method_decorator(login_required, name='dispatch')
class IncomeDetailView(DetailView):
    model = BudgetIncome

    def get_object(self, queryset=None):
        obj = get_object_or_404(Calculator.objects.get(user_id=self.request.user.pk).budgetincome_set, pk=self.kwargs['pk'])
        return obj


@method_decorator(login_required, name='dispatch')
class ExpensesDetailView(DetailView):
    model = BudgetExpenses

    def get_object(self, queryset=None):
        obj = get_object_or_404(Calculator.objects.get(user_id=self.request.user.pk).budgetexpenses_set, pk=self.kwargs['pk'])
        return obj


@method_decorator(login_required, name='dispatch')
class IncomeYearView(YearArchiveView):
    model = BudgetIncome
    date_field = 'date'
    make_object_list = True

    def get_queryset(self):
        return BudgetIncome.objects.filter(calculator__user=self.request.user)


@method_decorator(login_required, name='dispatch')
class IncomeMonthView(MonthArchiveView):
    model = BudgetIncome
    date_field = 'date'

    def get_queryset(self):
        return BudgetIncome.objects.filter(calculator__user=self.request.user)
