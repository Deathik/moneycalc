from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'calculator'
urlpatterns = [
    url(r'^$', login_required(views.budget_edit), name='budget_edit'),
    url(r'^add_budget/$', login_required(views.BudgetAddView.as_view()), name='add_budget'),
    url(r'^del_budget/$', login_required(views.BudgetExpensesView.as_view()), name='del_budget'),
    url(r'^income/$', login_required(views.IncomeList.as_view()), name='all_income_list'),
    url(r'^expenses/$', login_required(views.ExpensesList.as_view()), name='all_expenses_list'),
    url(r'^income/detail/(?P<pk>[0-9]+)/$', login_required(views.IncomeDetailView.as_view()), name='income_detail'),
    url(r'^expenses/detail/(?P<pk>[0-9]+)/$', login_required(views.ExpensesDetailView.as_view()), name='expenses_detail'),
    url(r'^income/(?P<year>[0-9]+)/$', login_required(views.IncomeYearView.as_view()), name='income_year'),
    url(r'^income/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
        login_required(views.IncomeMonthView.as_view(month_format='%m')), name='income_month'),
]
