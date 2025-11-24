import json
import os
from datetime import datetime

# Load saved transactions
def load_data():
    if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as f:
            return json.load(f)
    return []

# Save transactions to file
def save_data(data):
    with open("expenses.json", "w") as f:
        json.dump(data, f, indent=4)

#Add a transaction
def add_transaction(trans_type, amount, category, description):
    data = load_data()
    transaction = {
        "type": trans_type,                    # income or expense
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    data.append(transaction)
    save_data(data)
    print("Transaction added successfully.")

#View all transactions
def view_transactions():
    data = load_data()
    if not data:
        print("No transactions recorded yet.")
        return

    print("\n--- All Transactions ---")
    for i, t in enumerate(data, 1):
        print(f"{i}. [{t['date']}] {t['type'].upper()} - Rs.{t['amount']} "
              f"({t['category']}) - {t['description']}")

# View income/expense summary
def view_summary():
    data = load_data()
    total_income = sum(t["amount"] for t in data if t["type"] == "income")
    total_expense = sum(t["amount"] for t in data if t["type"] == "expense")
    balance = total_income - total_expense

    print("\n--- Summary ---")
    print(f"Total Income: Rs.{total_income}")
    print(f"Total Expense: Rs.{total_expense}")
    print(f"Current Balance: Rs.{balance}")

# View spending by category
def view_by_category(category):
    data = load_data()
    filtered = [t for t in data if t["type"] == "expense" and t["category"] == category]

    if not filtered:
        print(f"No expenses found for category '{category}'.")
        return

    total = sum(t["amount"] for t in filtered)

    print(f"\nTotal spent on {category}: Rs.{total}")
    print("Details:")
    for t in filtered:
        print(f"- Rs.{t['amount']} on {t['date']} ({t['description']})")


# Main Menu Loop
def main():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. View Summary")
        print("5. View Expense by Category")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Amount: "))
            category = input("Category: ")
            desc = input("Description: ")
            add_transaction("income", amount, category, desc)

        elif choice == "2":
            amount = float(input("Amount: "))
            category = input("Category: ")
            desc = input("Description: ")
            add_transaction("expense", amount, category, desc)

        elif choice == "3":
            view_transactions()

        elif choice == "4":
            view_summary()

        elif choice == "5":
            cat = input("Enter category name: ")
            view_by_category(cat)

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    main()
