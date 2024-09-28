from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense, UserIncome, Budget
from django.db.models import Sum
from django.contrib import messages
from decimal import Decimal

def index(request):
    if request.method == "POST":
        # Handle income setting
        if 'set_budget' in request.POST:
            income = request.POST.get('income')
            limit = request.POST.get('budget_limit')
            try:
                income = Decimal(income)
                limit = Decimal(limit)

                # Set user income
                user_income, created = UserIncome.objects.get_or_create(id=1)  # Assuming a single income entry
                user_income.income = income
                user_income.save()

                # Set budget
                Budget.objects.update_or_create(id=1, defaults={'limit': limit})
                messages.success(request, f"Budget set to ₹{limit}")
            except ValueError:
                messages.error(request, 'Invalid income or budget value')
            return redirect('/')
        
        # Handle expense submission
        expense_name = request.POST.get('expname')
        amount = request.POST.get('expnamount')
        category = request.POST.get('expcategory')


        if expense_name and amount and category:
            try:
                amount = int(amount)
                # Create the expense object
                Expense.objects.create(
                    expense_name=expense_name,
                    amount=amount,
                    category=category,
                )
                return redirect('/')  # Redirect after form submission
            except ValueError:
                return render(request, 'index.html', {'error': 'Invalid amount value'})
        else:
            return render(request, 'index.html', {'error': 'All fields are required'})

    # Fetch and display all expenses
    expenses = Expense.objects.all().order_by('-created_at')
    budgets = Budget.objects.all()
    
    # Fetch user's income
    user_income = UserIncome.objects.first()
    income = user_income.income if user_income else Decimal(0)

    # Calculate total expenses
    total_expenses = Expense.objects.aggregate(total=Sum('amount'))['total'] or Decimal(0)

    # Calculate remaining balance
    remaining_balance = income - total_expenses

    budget_notifications = []
    if budgets:
        total_budget_limit = budgets[0].limit  # Assuming only one budget
        # Check for the 'deleting' query parameter
        if request.GET.get('deleting') != 'true':
            if total_expenses > total_budget_limit:
                messages.success(request, f"Budget exceeded! Limit: ₹{total_budget_limit}")

    categories, data = expense_list()  


    return render(request, 'index.html', {
        'expenses': expenses,
        'remaining_balance': remaining_balance,
        'total_expenses': total_expenses,
        'income': income,
        'budgets': budgets,
        'budget_notifications': budget_notifications,
        'categories': categories,
        'data': data,
    })


def delete_expense(request, expense_id):
    if request.method == 'POST':
        expense = get_object_or_404(Expense, pk=expense_id)
        expense.delete()
        messages.success(request, "Expense deleted successfully.")
        # Redirect with a query parameter indicating a deletion
        return redirect('/?deleting=true')
    return redirect('/')


def delete_all_expenses(request):
    if request.method == "POST":
        Expense.objects.all().delete()
        messages.success(request, "All expenses cleared.")
        return redirect('/')
    return redirect('/')

def expense_list():
    expenses = Expense.objects.all()

    # Example data aggregation (customize according to your needs)
    categories = ['Food', 'Rent', 'Groceries', 'Transport','Shopping','Entertainment','Other']
    data = [0, 0, 0, 0, 0, 0, 0]  # Initialize counts for each category

    for expense in expenses:
        if expense.category == 'Food':
            data[0] += expense.amount
        elif expense.category == 'Rent':
            data[1] += expense.amount
        elif expense.category == 'Groceries':
            data[2] += expense.amount
        elif expense.category == 'Transport':
            data[3] += expense.amount
        elif expense.category == 'Shopping':
            data[4] += expense.amount
        elif expense.category == 'Entertainment':
            data[5] += expense.amount
        elif expense.category == 'Other':
            data[6] += expense.amount

    return categories, data