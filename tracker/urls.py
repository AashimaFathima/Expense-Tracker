from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    path('delete_all_expenses/', views.delete_all_expenses, name='delete_all_expenses'),
]

