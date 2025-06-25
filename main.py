from expense_tracker import add_expense, list_expenses, summarize_by_category, save_expenses, load_expenses

load_expenses("expenses.txt")
add_expense("Coffee", "15.50", "Food")
add_expense("Bus ticket", "10.00", "Transport")
add_expense("Lunch", "20.00", "Food")
list_expenses()
summarize_by_category()
save_expenses("expenses.txt")