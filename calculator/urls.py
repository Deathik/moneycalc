from django.conf.urls import url
from . import views

app_name = 'calculator'
urlpatterns = [
    url(r'^$', views.budget_edit, name='budget_edit'),
    url(r'^base/$', views.base),
    url(r'^add_budget/$', views.add_budget, name='add_budget'),
    url(r'del_budget/$', views.del_budget, name='del_budget'),
]
