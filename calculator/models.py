from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .validators import more_than_zero_validator


class Calculator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def inc_budget(self, value):
        if value <= 0:
            raise ValidationError(_("Can't be negative"))
        else:
            self.budget += value
            return self.budget

    def dec_budget(self, value):
        if value <= 0:
            raise ValidationError(_("Can't be negative"))
        else:
            self.budget -= value
            return self.budget

    def __str__(self):
        return "{}'s budget".format(self.user)


class BudgetAbstract(models.Model):
    calculator = models.ForeignKey(Calculator, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                validators=[more_than_zero_validator])
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-date']

    def __str__(self):
        return "{}: {}".format(self.calculator.user.username, self.value)


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
