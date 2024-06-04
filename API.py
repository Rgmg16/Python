# Making a basic GET request
# import requests

# response = requests.get('https://api.example.com/data')
# print(response.status_code)  # 200 means success
# print(response.json())  # Print the JSON response

# Handling responses
# data = response.json()
# print(data['key'])  # Accessing specific data from the JSON response

# Error handling
# if response.status_code == 200:
#     data = response.json()
# else:
#     print('Failed to retrieve data:', response.status_code)

# Using query parameters
# parames = {
#     'param1': 'value1',
#     'param2': 'value2'
# }
# response = requests.get('https://api.example.com/data', params=parames)
# print(response.json())

# Making POST requests
# payload = {
#     'key1': 'value1',
#     'key2': 'value2'
# }
# response = requests.post('https://api.example.com/data', json=payload)
# print(response.json())

# Authentication
# 1. API keys

# headers = {
#     'Authorization': 'Bearer YOUR_API_KEY'
# }
# response = requests.get('https://api.example.com/data', headers=headers)
# print(response.json())

# Sample API use
# 1. Fetching data

# import requests

# api_key = 'e271d6e1b910766254ec39bc7dcf2d1f'
# city = 'London'
# url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# response = requests.get(url)
# data = response.json()

# if response.status_code == 200:
#     print(f"City: {data['name']}")
#     print(f"Temperature: {data['main']['temp']}K")
#     print(f"Weather: {data['weather'][0]['description']}")
# else:
#     print('Failed to retrieve data:', response.status_code)

# 2. Pushing data using POST
# import requests

# url = "https://fakestoreapi.com/products"
# data = {
#     "title": "New Product",
#     "price": 29.99,
#     "description": "A new product description",
#     "image": "https://i.pravatar.cc",
#     "category": "electronics"
# }

# response = requests.post(url, json=data)

# if response.status_code == 200:
#     print("Data pushed successfully:", response.json())
# else:
#     print("Failed to push data:", response.status_code, response.text)

# 3. Updating data using PUT
# import requests

# product_id = 1  # Replace with the ID of the product you want to update
# url = f"https://fakestoreapi.com/products/{product_id}"
# data = {
#     "title": "Updated Product",
#     "price": 39.99,
#     "description": "An updated product description",
#     "image": "https://i.pravatar.cc",
#     "category": "electronics"
# }

# response = requests.put(url, json=data)

# if response.status_code == 200:
#     print("Data updated successfully:", response.json())
# else:
#     print("Failed to update data:", response.status_code, response.text)

# 4. Deleting of data using DELETE
import requests

product_id = 1  # Replace with the ID of the product you want to delete
url = f"https://fakestoreapi.com/products/{product_id}"

response = requests.delete(url)

if response.status_code == 200:
    print("Data deleted successfully:", response.json())
else:
    print("Failed to delete data:", response.status_code, response.text)
