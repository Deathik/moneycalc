from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class TestCalculatorModel(TestCase):
    def test_calculator_exists_after_user_creation(self):
        # Checks if Calculator exists after user registration
        user = User.objects.create(username='test')
        self.client.force_login(user=user)
        self.assertIsNotNone(user.calculator)


class TestIncomeViews(TestCase):
    def test_empty_income_list(self):
        # Testing Users without income
        user = User.objects.create(username='test')
        self.client.force_login(user=user)
        response = self.client.get(reverse('calculator:all_income_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You have no income yet")
        self.assertQuerysetEqual(response.context['budgetincome_list'], [])


class TestExpensesViews(TestCase):
    def test_empty_expenses_list(self):
        # Testing Users without expenses
        user = User.objects.create(username='test')
        self.client.force_login(user=user)
        response = self.client.get(reverse('calculator:all_expenses_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You have no expenses yet")
        self.assertQuerysetEqual(response.context['budgetexpenses_list'], [])