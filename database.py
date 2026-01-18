import sqlite3
from expense import Expense

db_name = 'expenses.db'

def get_connection():
    return sqlite3.connect(db_name)

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   amount REAL NOT NULL,
                   category TEXT NOT NULL
                    )
''')
    
    conn.commit()
    conn.close()

def add_expense(expense:Expense):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
                    "INSERT INTO expenses (name,amount,category) VALUES (?, ?, ?)",
                    (expense.name, expense.amount, expense.category)
                    )

    conn.commit()
    conn.close()

def get_all_expenses():
    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name, amount, category FROM expenses")
    rows = cursor.fetchall()

    conn.close()

    expenses = []
    for name, amount, category in rows:
        expenses.append(
            Expense(name=name,amount=amount,category=category)
        )

    return expenses

def delete_expenses_by_id(expense_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id))

    conn.commit()
    conn.close()

def update_expense(expense_id: int, new_expense:Expense):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""UPDATE expenses
                    SET name = ?, amount = ? , category = ?
                    WHERE id = ?
                   """, (new_expense.name,new_expense.amount,new_expense.category,expense_id ))
    
    conn.commit()
    conn.close()