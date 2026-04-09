import sqlite3

# This creates a file to save your money info
connection = sqlite3.connect('my_money.db')
cursor = connection.cursor()

# This creates a "table" (like an Excel sheet)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        item TEXT,
        price REAL
    )
''')

connection.commit()
connection.close()
print("Database is ready!")
