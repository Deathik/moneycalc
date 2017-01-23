import decimal

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Calculator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def inc_budget(self, value):
        self.budget += value
        return self.budget

    def dec_budget(self, value):
        self.budget -= value
        return self.budget

    def __str__(self):
        return "{}'s budget".format(self.user)


class BudgetExpenses(models.Model):
    calculator = models.ForeignKey(Calculator, on_delete=models.CASCADE)
    value = models.DecimalField(
        max_digits=10, decimal_places=2, default=0,
        validators=[
            MinValueValidator(decimal.Decimal(0.01), message="Can't be negative")
            ]
         )
    category_choices = (
            ('FD', 'Food'),
            ('CL', 'Clothes'),
            ('EN', 'Entertainment'),
            ('BL', 'Bills'),
            ('OT', 'Other'),
            )
    category = models.CharField(max_length=2, choices=category_choices)
    date = models.DateTimeField(auto_now_add=True)


class BudgetIncome(models.Model):
    calculator = models.ForeignKey(Calculator, on_delete=models.CASCADE)
    value = models.DecimalField(
        max_digits=10, decimal_places=2, default=0,
        validators=[
            MinValueValidator(decimal.Decimal(0.01), message="Can't be negative")
            ]
         )
    category_choices = (
        ('SL', 'Salary'),
        ('DP', 'Deposit'),
        ('OT', 'Other'),
    )
    category = models.CharField(max_length=2, choices=category_choices)
    date = models.DateTimeField(auto_now_add=True)
