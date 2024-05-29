# Matching examples
# 1. Matching an email address
import re

text = "Contact us at info@example.com or support@example.net"
matches = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
print(matches)  # Output: ['info@example.com', 'support@example.net']

# 2.Matching dates

text = "Today's date is 05/29/2024 and tomorrow's date is 05/30/2024"
matches = re.findall(r'\d{2}/\d{2}/\d{4}', text)
print(matches)  # Output: ['05/29/2024', '05/30/2024']

# 3.Matching HTML tags

html = "<h1>Hello</h1><p>This is a paragraph</p>"
tags = re.findall(r'<[^>]+>', html)
print(tags)  # Output: ['<h1>', '</h1>', '<p>', '</p>']

# Extracting examples
# 1. Extracting phone numbers

text = "Contact us at 123-456-7890 or 987-654-3210"
phone_numbers = re.findall(r'\d{3}-\d{3}-\d{4}', text)
print(phone_numbers)  # Output: ['123-456-7890', '987-654-3210']

# 2. Extracting URLs

text = "Visit our website at https://www.example.com or check out our blog at http://blog.example.com"
urls = re.findall(r'https?://\S+', text)
print(urls)  # Output: ['https://www.example.com', 'http://blog.example.com']

# 3. Extracting hashtags

text = "This is a #regex example. #Python is awesome!"
hashtags = re.findall(r'#\w+', text)
print(hashtags)  # Output: ['#regex', '#Python']
