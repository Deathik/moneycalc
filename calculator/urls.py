from django.conf.urls import url
from . import views

app_name = 'calculator'
urlpatterns = [
    url(r'^$', views.budget_edit, name='budget_edit'),
    url(r'^add_budget/$', views.add_budget, name='add_budget'),
    url(r'del_budget/$', views.del_budget, name='del_budget'),
url(r'^(?P<year>[0-9]{4})/$',
        views.IncomeYear.as_view(),
        name="year_budget"),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
        views.IncomeMonth.as_view(month_format='%m'),
        name="month_budget"),
]
