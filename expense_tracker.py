import os

expenses = []


def add_expense(description, amount, category):
    try:
        amount = float(amount)
    except ValueError:
        print("Error: Amount must be a number")
        return

    new_id = len(expenses) + 1
    expense = {"id": new_id, "description": description, "amount": amount, "category": category}
    expenses.append(expense)
    print(f"Added expense: {description}, {amount}, {category}")

def list_expenses():
    if len(expenses) == 0:
        print("No expenses")
        return
    else:
        for expense in expenses:
            print(f"ID: {expense['id']}, Description: {expense['description']}, Amount: {expense['amount']}, Category: {expense['category']}")


def summarize_by_category():
    if len(expenses) == 0:
        print("No expenses")
        return
    else:
        totals = {}
        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]
            if category not in totals:
                totals[category] = 0
            totals[category] += amount
        for category in totals:
            print(f"{category}: {totals[category]}")


def save_expenses(filename):
    if len(expenses) == 0:
        print("No expenses")
        return

    else:
        with open(filename, "w") as file:
            for expense in expenses:
                file.write(f"{expense['id']},{expense['description']},{expense['amount']},{expense['category']}\n")


def load_expenses(filename):
    if len(expenses) == 0:
        print("No expenses")
        return

    else:
        import os
        if not os.path.exists(filename):
            return

        else:
            with open(filename, "r") as file:

                for line in file:
                    parts = line.strip().split(",")

                    expense = {"id": int(parts[0]),
                               "description": parts[1],
                               "amount": float(parts[2]),
                               "category": parts[3]}

                    expenses.append(expense)