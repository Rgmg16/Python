# Reading JSON
import json

# JSON string
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Parse JSON string to Python dictionary
data = json.loads(json_string)
print(data["name"])  # Output: John

# Writing JSON

# Python dictionary
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert Python dictionary to JSON string
json_string = json.dumps(data)
print(json_string)  # Output: {"name": "John", "age": 30, "city": "New York"}
