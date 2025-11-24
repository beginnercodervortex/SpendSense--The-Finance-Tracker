# SpendSense--The-Finance-Tracker
A simple Python-based application for recording, managing, and analyzing daily income and expenses. The system stores all financial transactions in a JSON file and provides clear summaries to help users understand their spending patterns.

# Features

- Add income and expense transactions
- View all recorded transactions
- Get total income, total expense, and current balance
- View expenses filtered by category
- Automatic date logging
- Data persistence using JSON (no external database required)

# How It Works

The program stores every transaction in a JSON file (expenses.json). Each transaction contains:
- Type (income/expense)
- Amount
- Category
- Description
- Date
- Users interact with a menu-driven interface to perform all actions.

# Tech Stack

- Python 3
- JSON for lightweight data storage
- Datetime for automatic date handling
- OS module for file management

# Project Structure
Expense-Tracker<br> 
├──> expenses.json     # Stores transaction data (auto-created)<br>
├──> expense_tracker.py # Main program file<br>
└──> README.md          # Project documentation<br>

# How to Run
- Install Python 3
- Download the project files
- Open a terminal in the project folder
- Run the program:
     <br> python expense_tracker.py

# Sample Output
--- Personal Expense Tracker ---
1. Add Income
2. Add Expense
3. View All Transactions
4. View Summary
5. View Expense by Category
6. Exit

# Why This Project?

This project solves a real-world problem by helping users track their finances without needing complex tools or databases. It is fully written in Python and ideal for beginners learning file handling, data structures, and modular programming.

# Future Improvements
- Edit/Delete transactions
- Monthly spending reports
- Category-wise pie charts
- GUI version using Tkinter
