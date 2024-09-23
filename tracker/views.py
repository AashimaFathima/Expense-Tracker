from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense, UserIncome
from django.db.models import Sum
from django.contrib import messages

def index(request):
    if request.method == "POST":
        if 'set_income' in request.POST:
            # Handle setting income
            try:
                income = int(request.POST.get('income'))
                user_income, created = UserIncome.objects.get_or_create(pk=1)
                previous_income = user_income.income
                user_income.income = income
                user_income.save()
                
                # Update previous stored income only if income has changed
                if previous_income != income:
                    request.session['previous_stored_income'] = previous_income
                
                # Reset message flag and session data
                request.session['message_displayed'] = False
                return redirect('/')  # Redirect after setting income
            except ValueError:
                return render(request, 'index.html', {'error': 'Invalid income value'})

        # Handle expense submission
        expense_name = request.POST.get('expname')
        amount = request.POST.get('expnamount')
        category = request.POST.get('expcategory')

        # Handling new data submitted by the user
        user_income = UserIncome.objects.first()
        income = user_income.income if user_income else 0

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
    user_income = UserIncome.objects.first()
    income = user_income.income if user_income else 0

    # Calculate total expenses
    total_expenses = Expense.objects.aggregate(total=Sum('amount'))['total']
    total_expenses = total_expenses if total_expenses is not None else 0

    # Calculate remaining balance
    remaining_balance = income - total_expenses

    # Get previous stored income from session
    previous_stored_income = request.session.get('previous_stored_income', None)

    # Determine if income has changed
    income_changed = previous_stored_income is not None and previous_stored_income != income


    # Check if the remaining balance is less than 0
    if remaining_balance < 0 and income_changed:
        if not request.session.get('message_displayed', False):
            messages.error(request, 'You have exceeded your income!')
            request.session['message_displayed'] = True

    if income==0:
        messages.error(request,'Income cannot be zero')



    return render(request, 'index.html', {  # Render the index.html template with context data
        'expenses': expenses,
        'remaining_balance': remaining_balance,
        'total_expenses': total_expenses,
        'income': income,
    })

def delete_expense(request, expense_id):
    if request.method == 'POST':
        expense = get_object_or_404(Expense, pk=expense_id)
        expense.delete()
        return redirect('/')
    return redirect('/')

def delete_all_expenses(request):
    if request.method == "POST":
        # Delete all Expense items
        Expense.objects.all().delete()
        
        # Redirect to the index page or another page after deletion
        return redirect('/')
    
    # If the method is not POST, return an error or redirect as needed
    return redirect('/')