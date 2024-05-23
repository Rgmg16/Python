#Accessing elements in strings using index
greeting= "Hello there"

print(greeting [1])

#String concatenation
string1="   Wassgood"
string2= "homie?"
string3= string1 + " " + string2

print(string3)

#String slicing
strng= "wagwan chief?"

substring= strng[0:13]
print(substring)

#String methods
# 1. Making all the characters uppercase
print(strng.upper())

#2. Making all the characters lowercase
print(strng.lower())

#3. Removing the whitespaces in a string
print(string1.strip())

#4. Replacing a string in a string
print(strng.replace("Wagwan","Wassgood"))

#5. Separating two strings in a string
print(strng.split())

#Methods of string formatting
#1. Using the percentage symbol

name= "Joe"
age=21

intro= "My name is %s and I am %d years old." %(name, age)
print(intro)

#2. Using the letter f
print(f"My name is {name} and I am {age} years old")

#3. Using the .format() method
print("My name is {} and I am {} years old".format(name, age))

#String built-in functions
#1. len(); returning the length of the string
print(len(strng))

#2. capitalize(); Capitalizing the first letter of a string
print(strng.capitalize())

#3. .title(); Capitalizes the first character of each word in the string
print(strng.title())

#4. .lower(); Makes all the letters in a string lowercase
print(strng.lower())
#5. .find(); Searches for the first occurrence of a substring in a string and returns the index at which the substring starts
print(strng.find('wag'))

#6. .replace(); Replaces all the occurrences of the old string with the new string
print(strng.replace("wagwan","Wassgood"))

#7. .join(); Returns a string in which the string elements have been joined by a separator
items=("apples","pears","bananas","and","guavas")
print(", ".join(items))

#8. .split(); Splits the string into substrings using the separator
str='The$earth$is$what$we$all$have$in$common'
print(str.split('$'))