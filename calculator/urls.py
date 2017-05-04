from django.conf.urls import url

from . import views

app_name = 'calculator'
urlpatterns = [
    url(r'^$', views.budget_edit, name='budget_edit'),
    url(r'^income_form/$', views.IncomeFormHandlerView.as_view(), name='income_form_handler'),
    url(r'^expenses_form/$', views.ExpensesFormHandlerView.as_view(), name='expenses_form_handler'),
    url(r'^income/$', views.IncomeList.as_view(), name='all_income_list'),
    url(r'^expenses/$', views.ExpensesList.as_view(), name='all_expenses_list'),
    url(r'^income/detail/(?P<pk>[0-9]+)/$', views.IncomeUpdateView.as_view(), name='income_detail'),
    url(r'^expenses/detail/(?P<pk>[0-9]+)/$', views.ExpensesUpdateView.as_view(), name='expenses_detail'),
    url(r'^income/delete/(?P<pk>\d+)/$', views.IncomeDeleteView.as_view(), name='income_delete'),
    url(r'^expenses/delete/(?P<pk>\d+)/$', views.ExpensesDeleteView.as_view(), name='expenses_delete'),
    url(r'^income/(?P<year>[0-9]+)/$', views.IncomeYearView.as_view(), name='income_year'),
    url(r'^income/(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$', views.IncomeMonthView.as_view(month_format='%m'),
        name='income_month'),
]
