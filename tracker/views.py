from django.shortcuts import render, redirect
from .models import Expense

def index(request):
    if request.method == "POST":
        expense_name = request.POST.get('expname')
        amount = request.POST.get('expnamount')
        category = request.POST.get('expcategory')

        # Create the expense object
        Expense.objects.create(
            expense_name=expense_name,
            amount=amount,
            category=category,
        )
        return redirect('/')  # Redirect after form submission

    # Fetch and display all expenses
    expenses = Expense.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'expenses': expenses})
