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

    def list_expenses(self, category=None):
        try:
            query = 'SELECT id, description, amount, category FROM expenses'
            params = []

            if category:
                query += ' WHERE category = ?'
                params.append(category)

            self.cursor.execute(query, params)
            expenses = self.cursor.fetchall()
            return expenses

        except sqlite3.Error as e:
            print(f"שגיאה ברשימת הוצאות: {e}")
            return []


    def delete_expense(self, expense_id):
        try:
            self.cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
            self.conn.commit()
            if self.conn.total_changes > 0:
                print(f"expense deleted with id: {expense_id}")
                return True

            else:
                print(f"no expense found with id: {expense_id}")
                return False

        except sqlite3.Error as e:
            print(f" error deleting expense: {e}")
            return False


    def summarize_by_category(self, min_amount=None):
        try:
            query = 'SELECT category, SUM(amount) as total FROM expenses'
            params = []

            if min_amount is not None:
                query += ' WHERE amount >= ?'
                params.append(min_amount)

            query += ' GROUP BY category'
            self.cursor.execute(query, params)

            totals = self.cursor.fetchall()
            return totals

        except sqlite3.Error as e:
            print(f"error summarizing by category: {e}")
            return []

    def __del__(self):
        self.conn.close()