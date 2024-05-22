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