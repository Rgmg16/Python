import re

# Basic pattern matching using search()

pattern = "Python"
text = "I write code in Python."
match = re.search(pattern, text)
print("Match found:", bool(match))

# Using findall() to find all occurrences of a pattern
pattern = "a"
text = "I love to code in Python and it's amazing!"
matches = re.findall(pattern, text)
print("Matches found:", len(matches))

# Using split() to split a string based on a pattern
pattern = "\s"
text = "I like Python and it is amazing!"
split_text = re.split(pattern, text)
print("Split text:", split_text)

# Using sub() to replace a pattern with a string
pattern = "Python"
replacement = "Java"
text = "Python is fun"
substituted_text = re.sub(pattern, replacement, text)
print("Substituted text:", substituted_text)

# Using ^ to match the start of a string
pattern = "^I"
text = "I love Python!"
match = re.search(pattern, text)
print("Match found:", bool(match))

# Using [] to create a character set
pattern = "[Pp]ython"
text = "I write code in python and Python!"
matches = re.findall(pattern, text)
print("Matches found:", len(matches))

# Using '.' to match any character
pattern = "Py...n"
text = "I love Python, Pyt3on, Py45n, and Py@#n!"
matches = re.findall(pattern, text)
print("Matches found:", len(matches))

# Using * to match zero or more occurrences of a character
pattern = "Py.*n"
count = 0
text = ["Python coding", "Pyt3on","Java", "Py45n", "Py@#n","Pyn"]
for i in text:
    if(re.findall(pattern, i)):
        count+=1
print("Matches found:", count)

# Using + to match one or more occurrences of a character
pattern = "Py.+n"
count = 0
text = ["Python coding", "Pyt3on","Java", "Py45n", "Py@#n","Pyn"]
for i in text:
    if(re.findall(pattern, i)):
        count+=1
print("Matches found:", count)

# Using ? to match zero or one occurrence of a character
pattern = "Py.?n"
count = 0
text = ["Python coding", "Pyt3on","Java", "Py45n", "Py@#n","Pyn"]
for i in text:
    if(re.findall(pattern, i)):
        count+=1
print("Matches found:", count)

# Using $ to match the end of a string
pattern = "Python!$"
text = "Python programming is great!"
match = re.search(pattern, text)
print("Match found:", bool(match))

#  Using {} to specify the number of occurrences of a character
pattern = "Py{1,2}n"
text = "I love Pyn, Pyyn, and Pyyyn!"
matches = re.findall(pattern, text)
print("Matches found:", len(matches))

# Using \d to match zero or one occurrence of a character

pattern = "\d+"
text = "My phone number is 123-456-7890."
matches = re.findall(pattern, text)
print(matches)
print("Matches found:", len(matches))

# Using \w to match alphanumeric characters
pattern = "\w+"
text = "I_love_Python!"
matches = re.findall(pattern, text)
print(matches)
print("Matches found:", len(matches))

# Using \s to match whitespace characters
pattern = "\s+"
text = "I love Python!"
matches = re.findall(pattern, text)
print("Matches found:", len(matches))

# Using '|' as an 'or' operator
pattern = "Python|Java"
text = "I write code in Python and Java!"
matches = re.findall(pattern, text)
print("Matches found:", len(matches))

# Using () to group patterns
pattern = "(\d{3})-(\d{3})-(\d{4})"
text = "My phone number is 123-456-7890."
match = re.search(pattern, text)
if match:
    print("Area code:", match.group(1))
    print("Local exchange:", match.group(2))
    print("Line number:", match.group(3))
    