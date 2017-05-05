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

    return render(request, 'calculator/index.html', {
        'inc_form': IncomeForm(),
        'exp_form': ExpensesForm(),
        'budget': total_inc - total_exp,
        'expenses': calc.budgetexpenses_set.all()[:5],
        'income': calc.budgetincome_set.all()[:5],
        'total_inc': total_inc,
        'total_exp': total_exp,
        })


@method_decorator(login_required, name='dispatch')
class IncomeFormHandlerView(generic.View):

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('calculator:budget_edit'))

    def post(self, request, *args, **kwargs):
        calc = Calculator.objects.get(user_id=self.request.user.pk)
        form = IncomeForm(self.request.POST)
        if form.is_valid():
            value = form.cleaned_data.get('value')
            changes = BudgetIncome(
                calculator=calc,
                value=value,
                category=form.cleaned_data.get('category'),
            )
            changes.save()
            calc.save()
            return HttpResponseRedirect(reverse('calculator:budget_edit'))
        else:
            messages.add_message(request, messages.ERROR, form.errors)
            return HttpResponseRedirect(reverse('calculator:budget_edit'))


@method_decorator(login_required, name='dispatch')
class ExpensesFormHandlerView(generic.View):
    
    def get(self, request):
        return HttpResponseRedirect(reverse('calculator:budget_edit'))

    def post(self, request, *args, **kwargs):
        calc = Calculator.objects.get(user_id=self.request.user.pk)
        form = ExpensesForm(self.request.POST)
    
        if form.is_valid():
            value = form.cleaned_data.get('value')
            changes = BudgetExpenses(
                calculator=calc,
                value=value,
                category=form.cleaned_data.get('category'),
            )
            changes.save()
            calc.save()
            return HttpResponseRedirect(reverse('calculator:budget_edit'))
        else:
            messages.add_message(request, messages.ERROR, form.errors)
            return HttpResponseRedirect(reverse('calculator:budget_edit'))


@method_decorator(login_required, name='dispatch')
class IncomeList(generic.ListView):
    model = BudgetIncome
    paginate_by = 10

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
    paginate_by = 10

    def get_queryset(self):
        return Calculator.objects.get(pk=self.request.user.pk).budgetexpenses_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_exp = Calculator.objects.get(pk=self.request.user.pk).budgetexpenses_set.all()
        total_exp = total_exp.aggregate(total=models.Sum(models.F('value')))
        context['total_exp'] = total_exp['total']
        return context


@method_decorator(login_required, name='dispatch')
class IncomeUpdateView(generic.UpdateView):
    model = BudgetIncome
    form_class = IncomeForm
    template_name = 'calculator/budgetincome_detail.html'

    def get_success_url(self):
        return reverse('calculator:budget_edit')

    def get_object(self, queryset=None):
        obj = get_object_or_404(
            Calculator.objects.get(user_id=self.request.user.pk).budgetincome_set, pk=self.kwargs['pk']
        )
        return obj


@method_decorator(login_required, name='dispatch')
class ExpensesUpdateView(generic.UpdateView):
    model = BudgetExpenses
    form_class = ExpensesForm
    template_name = 'calculator/budgetexpenses_detail.html'

    def get_success_url(self):
        return reverse('calculator:budget_edit')

    def get_object(self, queryset=None):
        obj = get_object_or_404(Calculator.objects.get(user_id=self.request.user.pk).budgetexpenses_set,
                                pk=self.kwargs['pk']
                                )
        return obj


@method_decorator(login_required, name='dispatch')
class IncomeDeleteView(generic.DeleteView):
    model = BudgetIncome
    template_name = 'calculator/income_delete.html'

    def get_success_url(self):
        return reverse('calculator:budget_edit')

    def get_object(self, queryset=None):
        return BudgetIncome.objects.filter(calculator__user=self.request.user).get(pk=self.kwargs['pk'])


@method_decorator(login_required, name='dispatch')
class ExpensesDeleteView(generic.DeleteView):
    model = BudgetExpenses
    template_name = 'calculator/expenses_delete.html'

    def get_success_url(self):
        return reverse('calculator:budget_edit')

    def get_object(self, queryset=None):
        return BudgetExpenses.objects.filter(calculator__user=self.request.user).get(pk=self.kwargs['pk'])


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
