# import sqlite3
# from expense import Expense

# db_name = 'expenses.db'

# def get_connection():
#     return sqlite3.connect(db_name)

import sqlite3
import os
from expense import Expense

DB_PATH = os.path.join(os.path.dirname(__file__), "expenses.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

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

    cursor.execute("SELECT id ,name, amount, category FROM expenses")
    rows = cursor.fetchall()

    conn.close()

    expenses = []
    for id, name, amount, category in rows:
        expenses.append(
            Expense(id=id, name=name,amount=amount,category=category)
        )

    return expenses

def get_expense_by_id(expense_id :int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name , amount, category FROM expenses WHERE id = ?",
                    (expense_id,)
                    )
    row = cursor.fetchone()
    conn.close()

    return row 


def delete_expense_in_db(expense_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))

    conn.commit()
    conn.close()

def update_expense_in_db(expense_id,name,amount,category):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""UPDATE expenses
                    SET name = ?, amount = ? , category = ?
                    WHERE id = ?
                   """, (name, amount, category, expense_id))
    
    conn.commit()
    conn.close()