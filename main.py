from ExpenseTrackerClass import ExpenseTrackerClass

def main():
    tracker = ExpenseTrackerClass()

    tracker.add_expense("קפה", 15.50, "אוכל")
    tracker.add_expense("אוטובוס", 10.00, "תחבורה")
    tracker.add_expense("ארוחת צהריים", 20.00, "אוכל")

    print("all expenses:")
    expenses = tracker.list_expenses()
    for exp in expenses:
        print(f"ID: {exp[0]}, description: {exp[1]}, amount: {exp[2]}, category: {exp[3]}")

    print("\ndeleting expense with ID 2:")
    tracker.delete_expense(2)

    print("\nexpenses after deletion:")
    expenses = tracker.list_expenses()
    for exp in expenses:
        print(f"ID: {exp[0]}, description: {exp[1]}, amount: {exp[2]}, category: {exp[3]}")

    print("\n summerize by category:")
    totals = tracker.summarize_by_category()
    for category, total in totals:
        print(f"category: {category}, total: {total}")

if __name__ == "__main__":
    main()