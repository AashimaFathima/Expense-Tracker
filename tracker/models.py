from django.db import models

# Create your models here.


class Expense(models.Model):
    category_choices=[
        ('Food','Food'),
        ('Rent', 'Rent'),
        ('Groceries', 'Groceries'),
        ('Transport', 'Transport'),
        ('Shopping', 'Shopping'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),
    ]
    created_at = models.DateTimeField(auto_now_add=True)
    expense_name = models.CharField(max_length=200)
    category = models.CharField(choices=category_choices, max_length=20)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.expense_name} - {self.amount}"

class UserIncome(models.Model):
    income = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Income: {self.income}"

class Budget(models.Model):
    limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.category}: {self.limit}"


