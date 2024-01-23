import re

user_input = input("Enter your date in any format: ")

# Lookahead pattern for keywords at the beginning of words
pattern = r"(?=\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)(?:uary|ruary|ch|ust|tember|ober|ember|y|e|il|\b)\b)"
# First part looks for words beginning in the specified three letters (Could catch words such as "Janitor")
# Second part searches the word for full month names or just the first three letters (will ignore words such as "Janitor")


# Find all matches
matches = re.findall(pattern, user_input, flags=re.IGNORECASE)

# Handle results
if matches:
    month = matches[0]  # Second group captures the actual keyword
    print(f"Extracted month: {month}")
else:
    print("No valid month keyword found.")
