import sqlite3
import ai_processor

# 1. Setup
api_key = "Your API key here"
user_input = input("Enter expense (e.g., '1500 for bike fuel'): ")

# 2. AI Logic
# AI returns something like "1500, Transport"
ai_result = ai_processor.analyze_spending(user_input, api_key)
amount, category = ai_result.split(",")

# 3. Save to Database
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO spending (description, amount, category) VALUES (?, ?, ?)", 
               (user_input, float(amount.strip()), category.strip()))
conn.commit()
conn.close()

print(f"✅ Saved: {amount.strip()} LKR in {category.strip()} category.")
