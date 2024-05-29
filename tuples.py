# An empty tuple
empty_tuple = ()

# A tuple with one element (note the comma)
single_element_tuple = (42,)

# A tuple with multiple elements
multiple_elements_tuple = (1, 'apple', 3.14, [1, 2, 3])

# Parentheses are optional when creating a tuple
another_tuple = 1, 'banana', 7.5

# Accessing tuple elements
my_tuple = (10, 20, 30, 40, 50)

# Access the first element
print(my_tuple[0])  # Output: 10

# Access the last element
print(my_tuple[-1])  # Output: 50

# Access a slice of the tuple
print(my_tuple[1:4])  # Output: (20, 30, 40)

# Tuple methods
# 1. count(): Returns the number of times a specified value occurs in a tuple.
# 2. index(): Searches the tuple for a specified value and returns the position of where it was found.

my_tuple = (10, 20, 30, 20, 40, 20)

# Count occurrences of 20
print(my_tuple.count(20))  # Output: 3

# Find the index of the first occurrence of 30
print(my_tuple.index(30))  # Output: 2

# Creating a new tuple by adding elements in another tuple to the one that already exists
original_tuple = (1, 2, 3)

# Attempt to modify a tuple will result in an error
# original_tuple[0] = 10  # This will raise a TypeError

# Creating a new tuple by concatenating tuples
new_tuple = original_tuple + (4, 5)
print(new_tuple)  # Output: (1, 2, 3, 4, 5)

# Use cases for tuples 

# 1. Returning multiple values from a function
def get_coordinates():
    x = 10
    y = 20
    return x, y  # Returns a tuple (10, 20)

coordinates = get_coordinates()
print(coordinates)  # Output: (10, 20)

# 2. Use as dictionary keys 
location = {
    (35.6895, 139.6917): "Tokyo",
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}

print(location[(35.6895, 139.6917)])  # Output: Tokyo
