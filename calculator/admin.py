from django.contrib import admin

from .models import Calculator, BudgetIncome, BudgetExpenses

admin.site.register(Calculator)
admin.site.register(BudgetIncome)
admin.site.register(BudgetExpenses)