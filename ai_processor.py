import google.generativeai as genai

# This function talks to the Gemini AI
def analyze_spending(user_text, my_key):
    genai.configure(api_key=my_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # We tell the AI exactly what we want back
    prompt = f"From this text: '{user_text}', extract the price and the category. Return it as: Price, Category. Example: 500, Food"
    
    response = model.generate_content(prompt)
    return response.text
