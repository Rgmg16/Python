#Creating a list
fruits= ["apple", "pear", "banana", "grape" ]

print (fruits [1])

#Negative indexing
print (fruits[-1])

#Adding to a list
fruits.append("mango")

print (fruits)

#Inserting an item in a list
fruits.insert(2,"cherry")

print(fruits)

#Removing the first instance of an item from a list
fruits.remove("pear")

print(fruits)

#Deleting a specific element in a list using del
del fruits[-1]

print (fruits)

#Deleting a specific element in a list using pop
fruits.pop(1)

print (fruits)

#Extending a list
moreFruits=["avocado", "orange","tomato"]
fruits.extend(moreFruits)

print(fruits)

#Getting a portion of a list
fruitsJnr= fruits[0:4:2]

print (fruitsJnr)

#Getting a protion of a list whilst skipping items in the list
print (fruitsJnr)

#Iterating through a list
for fruit in fruits:
    print(fruit)
    
#Finding the lenth of a list
length = len(fruits)

print(length)

#Sorting a list in alphabetical order
sortFruits= fruits.sort()

print (fruits)

#Reversing the order of the list
fruits.reverse()

print (fruits)

#Returning the index of the first instance of an element in a list
indexBanana=fruits.index("banana")

print(indexBanana)

#Checking the existence of an element in a list. It returns a boolean value.
guavaEx= "Guava" in fruits

print(guavaEx)

#Checking the number of occurrences of an element in a list
appleOc= fruits.count("apple")

print(appleOc)

#List comprehension: Creation of lists by applying an expression to each item in an existing iterable
#Example 1: generating squares of numbers
squares=[x**2 for x in range(5)]

print(squares)

#Example 2: Generating even numbers
evnNo=[x for x in range (10) if x%2==0]

print(evnNo)
    
        