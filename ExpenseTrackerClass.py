import sqlite3


class ExpenseTrackerClass:
    def __init__(self, db_name="expenses.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_expenses_table()


    def create_expenses_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL
            )
        ''')
        self.conn.commit()


    def add_expense(self, description, amount, category):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("ammount must be greater than zero")

            if not description or not category:
                raise ValueError("description and category are required")

            self.cursor.execute('''
                                INSERT INTO expenses (description, amount, category)
                                VALUES (?, ?, ?)
                                ''', (description, amount, category))
            self.conn.commit()

            print(f" expense added: {description}, {amount}, {category}")

        except (ValueError, sqlite3.Error) as e:
            print(f" error adding expense: {e}")


    def __del__(self):
        self.conn.close()