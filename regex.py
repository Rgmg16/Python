# Importing the 're' module

import re

# Checking for a match only at the beginning of a string using re.match()

pattern = r'\d+'  # Matches one or more digits
string = "123abc"
match = re.match(pattern, string)
if match:
    print("Match found:", match.group())
else:
    print("No match")

# Checking for a match anywhere in the string using re.search()

pattern = r'\d+'  # Matches one or more digits
string = "abc123"
match = re.search(pattern, string)
if match:
    print("Match found:", match.group())
else:
    print("No match")

# Returning a list of all matches in a string using re.findall()

pattern = r'\d+'  # Matches one or more digits
string = "abc123def456"
matches = re.findall(pattern, string)
print("All matches:", matches)

# Returning an iterator yielding matching objects for all matches in the string using re.finditer()

pattern = r'\d+'  # Matches one or more digits
string = "abc123def456"
matches = re.finditer(pattern, string)
for match in matches:
    print("Match found:", match.group(), "at position", match.start())


# Regex syntax

# . : Matches any character except newline.
# ^ : Matches the start of the string.
# $ : Matches the end of the string.
# * : Matches 0 or more repetitions of the preceding regex.
# + : Matches 1 or more repetitions of the preceding regex.
# ? : Matches 0 or 1 repetition of the preceding regex.
# {m,n} : Matches from m to n repetitions of the preceding regex.
# [abc] : Matches any one of the characters a, b, or c.
# [^abc] : Matches any character except a, b, or c.
# (abc) : Matches the group "abc".
# |: Alternation operator that matches either the expression before or after it.

# Regex modifiers
# i: Case-insensitive matching.
# m: Multiline mode where ^ and $ match the start and end of each line.
# s: Dot-all mode where . matches newline characters as well.
# x: Verbose mode that allows whitespace and comments within the pattern.