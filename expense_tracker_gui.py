import tkinter as tk
from tkinter import messagebox
from expense_tracker import add_expense, load_expenses, save_expenses, list_expenses
import io
from contextlib import redirect_stdout

def gui_main():
    window = tk.Tk()
    window.title("Expense Tracker")
    window.geometry("400x300")

    load_expenses("expenses.txt")

    description_label = tk.Label(window, text="Description")
    description_label.pack(pady=10, padx=10)

    description_entry = tk.Entry(window, width=30)
    description_entry.pack(pady=10, padx=10)

    amount_label = tk.Label(window, text="Amount")
    amount_label.pack(pady=10, padx=10)

    amount_entry = tk.Entry(window, width=30)
    amount_entry.pack(pady=10, padx=10)

    category_label = tk.Label(window, text="Category")
    category_label.pack(pady=10, padx=10)

    category_entry = tk.Entry(window, width=30)
    category_entry.pack(pady=10, padx=10)

    def add():
        description = description_entry.get()
        category = category_entry.get()
        amount = amount_entry.get()

        if description and category and amount:
            try:
                amount = float(amount)

                add_expense(description, amount, category)
                save_expenses("expenses.txt")
                messagebox.showinfo("Success", f"Added expense: {description}")

                description_entry.delete(0, tk.END)
                amount_entry.delete(0, tk.END)
                category_entry.delete(0, tk.END)

            except ValueError:
                messagebox.showerror("Error", "Invalid amount")

        else:
            messagebox.showerror("Error", "All fields required")

    add_expense_button = tk.Button(window, text="Add Expense", command=add)
    add_expense_button.pack(pady=10)

    filter_label = tk.Label(window, text="Filter by Category (optional)")
    filter_label.pack(pady=10, padx=10)

    filter_entry = tk.Entry(window, width=30)
    filter_entry.pack(pady=10, padx=10)

    text_area = tk.Text(window, height=10, width=50)
    text_area.pack(pady=10)

    def show_list():
        text_area.delete(1.0, tk.END)

        with io.StringIO() as buf, redirect_stdout(buf):
            category = filter_entry.get()
            list_expenses(category if category else None)

            output = buf.getvalue()

            text_area.insert(tk.END, output)

    list_button = tk.Button(window, text="List Expenses", command=show_list)
    list_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    gui_main()