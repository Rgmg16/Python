countrycapitals= {
    "Kenya": "Nairobi",
    "Uganda": "Kampala",
    "Tanzania": "Dodoma"
}

print(countrycapitals)

#Using the dict() function

numbers= dict(x=3, y=5)

print(numbers)

#Accessing the value of keys
print(countrycapitals["Kenya"])

#Adding an item to a dictionary
countrycapitals["Rwanda"] = "Kigali"

print(countrycapitals)

#Deleting an item from a dictionary
del(countrycapitals["Uganda"])

print(countrycapitals)

#Editing information in a dictionary
countrycapitals["Kenya"]= "Mombasa"

print(countrycapitals)

#Editing using the update() function
country1={"Kenya": "Kisumu"}
countrycapitals.update(country1)
print(countrycapitals)

#Looping through items in a dictionary
for country in countrycapitals:
    print(country)
    
#Removing an item with a specified key
countrycapitals.pop("Rwanda")

print(countrycapitals)

# Application of dictionaries
# 1. Storage of configuration settings

config = {
    'host': 'localhost',
    'port': 8080,
    'debug': True
}

# 2. Counting and frequency of items in a collection

from collections import Counter

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_count = Counter(words)
print(word_count)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})


# 3. Caching/Memoization: Stores results of expensive function calls to avoid redundant computations
cache = {}

def fibonacci(n):
    if n in cache:
        return cache[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = result
    return result

# 4. Data representation of complex data structures like graphs and trees.
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 5.Database records: Represents rows of data in a database or CSV file.
records = [
    {'id': 1, 'name': 'Alice', 'age': 25},
    {'id': 2, 'name': 'Bob', 'age': 30},
    {'id': 3, 'name': 'Charlie', 'age': 35}
]

