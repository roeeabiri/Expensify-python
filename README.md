Expense Tracker
Overview
Expense Tracker is a simple application for managing personal expenses. It allows users to add, delete, list, and summarize expenses by category. The project includes two interfaces:

Command Line Interface (CLI): Run commands in the terminal to manage expenses.
Graphical User Interface (GUI): A window-based interface for adding expenses using a form.

Expenses are stored in a file called expenses.txt.
Requirements

Python 3.6+: Ensure Python is installed on your system.
tkinter: Required for the GUI. Usually included with Python, but can be installed on Linux with:sudo apt-get install python3-tk



Installation

Clone or Download the Project:

If using Git, clone the repository:git clone <repository-url>
cd ExpensifyVENV


Or download and extract the project files to a folder (e.g., ExpensifyVENV).


Set Up a Virtual Environment (recommended):
python3 -m venv .
source bin/activate  # On Windows: .\Scripts\activate


Verify tkinter:

Run the following to check if tkinter is installed:python3 -c "import tkinter"


If you get an error, install tkinter:sudo apt-get install python3-tk





Usage
The project includes two main scripts: expense_tracker.py (CLI) and expense_tracker_gui.py (GUI).
CLI Usage
Run commands using expense_tracker.py to manage expenses via the terminal.
Available Commands

Add an expense:
python expense_tracker.py add "<description>" <amount> <category>

Example:
python expense_tracker.py add "Coffee" 15.50 Food

Adds an expense with description "Coffee", amount 15.50, and category "Food".

Delete an expense:
python expense_tracker.py delete <id>

Example:
python expense_tracker.py delete 1

Deletes the expense with ID 1.

List expenses:
python expense_tracker.py list [--category <category>]

Examples:
python expense_tracker.py list
python expense_tracker.py list --category Food

Lists all expenses or filters by category (e.g., "Food").

Summarize by category:
python expense_tracker.py summary [--min_amount <amount>]

Examples:
python expense_tracker.py summary
python expense_tracker.py summary --min_amount 10.0

Shows total expenses per category, optionally filtering by minimum amount.


Notes

Expenses are saved to expenses.txt after adding or deleting.
The file format is: id,description,amount,category (e.g., 1,Coffee,15.5,Food).

GUI Usage
Run the GUI to add expenses using a graphical interface.

Start the GUI:
python expense_tracker_gui.py


Features:

Enter a description, amount, and category in the provided fields.
Click "Add Expense" to add the expense.
If successful, a pop-up shows "Added expense: ", and the fields are cleared.
If there’s an error (e.g., empty fields or invalid amount), a pop-up shows the error.


Notes:

The GUI saves expenses to the same expenses.txt file as the CLI.
Currently, the GUI supports only adding expenses. Listing, deleting, and summarizing are available via the CLI.



Project Structure

expense_tracker.py: The CLI script for managing expenses.
expense_tracker_gui.py: The GUI script for adding expenses.
expenses.txt: The file where expenses are stored (created automatically when adding expenses).
README.md: This documentation file.

Example Workflow

Add expenses via CLI:python expense_tracker.py add "Lunch" 50.0 Food
python expense_tracker.py add "Bus" 10.0 Transport


List expenses:python expense_tracker.py list

Output:ID: 1, Description: Lunch, Amount: 50.0, Category: Food
ID: 2, Description: Bus, Amount: 10.0, Category: Transport


Add an expense via GUI:
Run python expense_tracker_gui.py.
Enter "Coffee", "15.50", "Food" in the fields and click "Add Expense".


Check the file:
Open expenses.txt to see:1,Lunch,50.0,Food
2,Bus,10.0,Transport
3,Coffee,15.5,Food





Future Improvements

Add GUI support for listing, deleting, and summarizing expenses.
Improve GUI layout with better styling or additional features (e.g., dropdown for categories).

Troubleshooting

CLI error: "No such file or directory":
Ensure expenses.txt is in the same folder as the scripts, or it will be created on first save.


GUI error: "No module named tkinter":
Install tkinter with sudo apt-get install python3-tk.


GUI doesn’t save expenses:
Ensure expense_tracker.py and expense_tracker_gui.py are in the same folder.


