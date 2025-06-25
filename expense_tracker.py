

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
    else:
        for expense in expenses:
            print(f"ID: {expense['id']}, Description: {expense['description']}, Amount: {expense['amount']}, Category: {expense['category']}")

