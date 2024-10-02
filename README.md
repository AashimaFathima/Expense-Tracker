# 🧮 Expense Tracker 🧮
An easy-to-use expense tracker that helps you manage your budget by allowing you to set a budget, track expenses, and visualize your spending with a pie chart.

This is my first Django project 🎉 and is designed to give users a smooth way to manage their daily finances.

## Features ✨
- **Set Budget:** Enter your total income and spending limit.
- **Add Expense:** Add an expense along with selecting the category from a dropdown menu.
- **Transaction Table:** View all your transactions in a table with the date, category, amount, and option to delete.
- **Pie Chart:** Visual representation of your expenses.
- **Total Summary:** Displays total income, total expenses, and remaining balance.
- **Alerts:**
Warns you if you exceed the budget 🚨
Shows confirmation when you delete an expense or all expenses ❌

## Future Features 🚀
- **Resolution Setting:** Allow users to adjust the screen resolution for better compatibility.
- **Expense Categories:** Enable users to add custom categories for expenses.
- **Export to CSV:** Add the ability to export expenses to a CSV file.
- **Monthly/Yearly Reports:** Generate detailed monthly or yearly reports for users to review their spending habits.
- **Currency Conversion:** Support for multiple currencies with automatic conversion rates.

## Installation 🛠️
### Prerequisites
Python 3.x installed on your machine
Django installed (run pip install django)
SQLite3 for database management
Git for cloning the repository

## Step-by-Step Guide 📋
**Clone the Repository:**
[git clone https://github.com/AashimaFathima/Expense-Tracker.git](https://github.com/AashimaFathima/Expense-Tracker.git)

**Navigate to the Project Directory:**
cd Expense-Tracker # or if renamed cd expensetracker

**Set up the Virtual Environment:**
python -m venv myenv
source myenv/bin/activate    # On Windows, use: myenv\Scripts\activate

**Install Dependencies:**
pip install -r requirements.txt

**Load the Database**
To load data into your MySQL database, use the following command:

```bash
mysql -u root -p expensetracker < dump.sql
```

**Run the Migrations:**
python manage.py migrate

**Start the Server:**
python manage.py runserver

You can now access the application on [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Screenshots 📸
![Landing Page-1](https://github.com/AashimaFathima/Expense-Tracker/blob/main/Screenshot%20(984).png)
![Landing Page-2](https://github.com/AashimaFathima/Expense-Tracker/blob/main/Screenshot%20(987).png)
![Transaction Table](https://github.com/AashimaFathima/Expense-Tracker/blob/main/Screenshot%20(986).png)
![Delete Expense Alert](https://github.com/AashimaFathima/Expense-Tracker/blob/main/Screenshot%20(988).png)
![Delete All Expenses Alert](https://github.com/AashimaFathima/Expense-Tracker/blob/main/Screenshot%20(989).png)


## Technologies Used 💻
Frontend: HTML, CSS, Bootstrap
Backend: Django (Python)
Database: MySQL

## Acknowledgments
Icons used from [FontAwesome](https://fontawesome.com) (Free Version)

## License 📜
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributions 🤝
Feel free to open an issue or create a pull request if you'd like to contribute!
