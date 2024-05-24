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