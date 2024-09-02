from django.db import models

# Create your models here.

class RemainingBalance(models.Model):
    remaining_balance=models.FloatField(default=0.0)

class Expense(models.Model):
    category_choices=[
        ('Food','Food'),
        ('Rent', 'Rent'),
        ('Groceries', 'Groceries'),
        ('Transport', 'Transport'),
        ('Shopping', 'Shopping'),
        ('Other', 'Other'),
    ]
    created_at = models.DateTimeField(auto_now_add=True)
    expense_name = models.CharField(max_length=200)
    category = models.CharField(choices=category_choices, max_length=20)
    amount = models.FloatField()

    def __str__(self):
        return f"{self.expense_name} - {self.amount}"

class TrackingHistory(models.Model):
    expense=models.ForeignKey(Expense, on_delete=models.CASCADE)
    remaining_balance=models.ForeignKey(RemainingBalance, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


