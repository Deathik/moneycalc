from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'calculator'
urlpatterns = [
    url(r'^$', views.budget_edit, name='budget_edit'),
    url(r'^income/$', views.IncomeList.as_view(), name='all_income_list'),
    url(r'^expenses/$', views.ExpensesList.as_view(), name='all_expenses_list'),
    url(r'^income/detail/(?P<pk>[0-9]+)/$', views.IncomeDetailView.as_view(), name='income_detail'),
    url(r'^expenses/detail/(?P<pk>[0-9]+)/$', views.ExpensesDetailView.as_view(), name='expenses_detail'),
    url(r'^income/(?P<year>[0-9]+)/$', views.IncomeYearView.as_view(), name='income_year'),
    url(r'^income/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$', views.IncomeMonthView.as_view(month_format='%m'),
        name='income_month'),
]
