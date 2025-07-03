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
        tracker.delete_expense(args.id)


    elif args.command == "list":
        expenses = tracker.list_expenses(args.category)

        if not expenses:
            print(f"אין הוצאות{' בקטגוריה ' + args.category if args.category else ''}")

        else:
            for exp in expenses:
                print(f"ID: {exp[0]}, description: {exp[1]}, amount: {exp[2]}, category: {exp[3]}")

    elif args.command == "summary":
        summarize_by_category(args.min_amount)

    else:
        parser.print_help()


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