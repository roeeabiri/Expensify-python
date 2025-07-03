import argparse
import os
import sqlite3
from ExpenseTrackerClass import ExpenseTrackerClass

def main():
    tracker = ExpenseTrackerClass()

    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add an expense")
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    list_parser = subparsers.add_parser("list", help="List all expenses")
    summary_parser = subparsers.add_parser("summary", help="Summarize expenses by categories")

    add_parser.add_argument("description", type=str, help="Description of expense")
    add_parser.add_argument("amount", type=float, help="Amount of expense")
    add_parser.add_argument("category", type=str, help="Category of expense")

    delete_parser.add_argument("id", type=int, help="ID of expense")

    list_parser.add_argument("--category", type=str, help="Filter by category", default=None)

    summary_parser.add_argument("--min_amount", type=float, help="Minimum amount of expense to be in the summary", default=None)

    args = parser.parse_args()

    if args.command == "add":
        try:
            tracker.add_expense(args.description, args.amount, args.category)

        except ValueError as e:
            print(e)


    elif args.command == "delete":
        delete_expense(args.id)
        save_expenses("expenses.txt")

    elif args.command == "list":
        list_expenses(args.category)

    elif args.command == "summary":
        summarize_by_category(args.min_amount)

    else:
        parser.print_help()


def delete_expense(id):
    if not expenses:
        print("No expenses to delete")
        return

    expense = next((e for e in expenses if e["id"] == id), None)

    if expense:
        expenses.remove(expense)
        print(f"Expense with ID {id} deleted")

        for i, e in enumerate(expenses, 1):
            e["id"] = i

    else:
        print(f"No expense found with ID {id}")


def list_expenses(category=None):
    if not expenses:
        print("No expenses")
        return

    found = False
    for expense in expenses:
        if category is None or expense["category"] == category:
            print(f"ID: {expense['id']}, Description: {expense['description']}, Amount: {expense['amount']}, Category: {expense['category']}")
            found = True

    if not found and category is not None:
        print(f"No expenses in category {category}")


def summarize_by_category(min_amount):
    if len(expenses) == 0:
        print("No expenses")
        return

    totals = {}
    for expense in expenses:
         category = expense["category"]
         amount = expense["amount"]

         if min_amount is None or amount >= min_amount:

            if category not in totals:
                totals[category] = 0

            totals[category] += amount

    if not totals:
        print(f"No expenses above {min_amount}" if min_amount is not None else "No expenses")
        return

    for category in totals:
        print(f"Category: {category}, Total: {totals[category]}")


def save_expenses(filename):
    if len(expenses) == 0:
        print("No expenses")
        return

    with open(filename, "w") as file:
        for expense in expenses:
            file.write(f"{expense['id']},{expense['description']},{expense['amount']},{expense['category']}\n")


def load_expenses(filename):
    expenses.clear()

    if not os.path.exists(filename):
        return

    with open(filename, "r") as file:
        for line in file:
            try:
                parts = line.strip().split(",")
                if len(parts) != 4:
                    continue

                expense = {
                    "id": int(parts[0]),
                    "description": parts[1],
                    "amount": float(parts[2]),
                    "category": parts[3]
                }

                expenses.append(expense)

            except (ValueError, IndexError):
                continue

if __name__ == "__main__":
    main()