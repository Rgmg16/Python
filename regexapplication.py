# 1. Text search and validation
#  a). Email validation

import re
email = "example@example.com"
if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
    print("Valid email address")
else:
    print("Invalid email address")

# b)Password strength checking

password = "Password123!"
if re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}$', password):
    print("Strong password")
else:
    print("Weak password")

# 2. Data extraction
# a) Extracting phone numbers

text = "Contact us at 123-456-7890 or 987-654-3210"
phone_numbers = re.findall(r'\d{3}-\d{3}-\d{4}', text)
print(phone_numbers)  # Output: ['123-456-7890', '987-654-3210']

# b)Extracting URLs

text = "Visit our website at https://www.example.com or check out our blog at http://blog.example.com"
urls = re.findall(r'https?://\S+', text)
print(urls)  # Output: ['https://www.example.com', 'http://blog.example.com']

# 3. Data tramsformation
# a)Replacing text patters

text = "Please contact support@example.com for assistance."
updated_text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', 'info@example.com', text)
print(updated_text)  # Output: "Please contact info@example.com for assistance."

# b)Splitting text

text = "The quick brown fox jumps over the lazy dog."
words = re.split(r'\W+', text)
print(words)  # Output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', '']
