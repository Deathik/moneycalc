from django.conf.urls import url
from . import views

app_name = 'calculator'
urlpatterns = [
    url(r'^$', views.budget_edit, name='budget_edit'),
    url(r'^add_budget/$', views.BudgetAddView.as_view(), name='add_budget'),
    url(r'^del_budget/$', views.BudgetExpensesView.as_view(), name='del_budget'),
    url(r'^income/$', views.AllIncomeList.as_view(), name='all_income_list'),
    url(r'^expenses/$', views.AllExpensesList.as_view(), name='all_expenses_list'),
]
