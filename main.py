import sqlite3
import ai_processor

# 1. Ask the user what they spent
print("--- AI Expense Tracker ---")
user_input = input("What did you buy today? ")

# 2. Get your Secret Key (You would type your key here locally)
api_key = "YOUR_KEY_HERE"

# 3. Use AI to understand the text
result = ai_processor.analyze_spending(user_input, api_key)
print(f"AI suggests: {result}")

# 4. Save it to the database
# (In the next step, we will make this automatic!)
