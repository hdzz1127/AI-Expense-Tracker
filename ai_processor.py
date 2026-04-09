def analyze_spending(user_text, api_key=None):
    keywords = {
        "food": ["burger", "food", "lunch", "dinner", "breakfast", "rice", "pizza", "coffee", "meal", "snack", "restaurant"],
        "transport": ["fuel", "bike", "bus", "taxi", "uber", "train", "petrol", "gas", "fare"],
        "shopping": ["shirt", "shoes", "clothes", "dress", "bag", "phone", "laptop", "book"],
        "health": ["medicine", "doctor", "hospital", "pharmacy", "gym"],
        "bills": ["electricity", "water", "internet", "rent", "bill"],
    }
    text = user_text.lower()

    price = None
    for word in text.split():
        cleaned = word.replace(",", "")
        if cleaned.isdigit():
            price = cleaned
            break

    category = "Other"
    for cat, words in keywords.items():
        if any(word in text for word in words):
            category = cat.capitalize()
            break

    return f"Price: {price}, Category: {category}"
