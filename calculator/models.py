import decimal

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Calculator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_inc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_exp = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def inc_budget(self, value):
        self.budget += value
        self.total_inc += value
        return self.budget

    def dec_budget(self, value):
        self.budget -= value
        self.total_exp += value
        return self.budget

    def __str__(self):
        return "{}'s budget".format(self.user)


class BudgetAbstract(models.Model):
    calculator = models.ForeignKey(Calculator, on_delete=models.CASCADE)
    value = models.DecimalField(
        max_digits=10, decimal_places=2, default=0,
        validators=[
            MinValueValidator(decimal.Decimal(0.01), message="Can't be negative")
        ]
    )
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-date']


class BudgetExpenses(BudgetAbstract):
    category_choices = (
            ('FD', 'Food'),
            ('CL', 'Clothes'),
            ('EN', 'Entertainment'),
            ('BL', 'Bills'),
            ('OT', 'Other'),
            )
    category = models.CharField(max_length=2, choices=category_choices)


class BudgetIncome(BudgetAbstract):
    category_choices = (
        ('SL', 'Salary'),
        ('DP', 'Deposit'),
        ('OT', 'Other'),
    )
    category = models.CharField(max_length=2, choices=category_choices)