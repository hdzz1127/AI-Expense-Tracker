import ai_processor

user_input = input("Enter expense (e.g., '1500 for bike fuel'): ")

ai_result = ai_processor.analyze_spending(user_input)

print(f"AI Analysis: {ai_result}")
