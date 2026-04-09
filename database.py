import sqlite3

# 1. Connect to a database file (it creates it if it doesn't exist)
connection = sqlite3.connect('expenses.db')
cursor = connection.cursor()

# 2. Create a table to store your spending
# We store: What it was, how much it cost, and the category (like 'Food' or 'Transport')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS spending (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        amount REAL,
        category TEXT
    )
''')

connection.commit()
connection.close()
print("Success! Your database is ready to store expenses.")
