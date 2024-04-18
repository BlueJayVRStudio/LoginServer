import requests
import json

# The URL to which the POST request is to be sent
url = 'http://127.0.0.1/users/login'

# Data to be sent, can be a dictionary
data = {
    'username': 'jay',
    'password': 'password1234'
}

# Convert the dictionary to a JSON string
json_data = json.dumps(data)

# Headers to indicate that the payload is in JSON format
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post('http://127.0.0.1/delete-user/someTestUser', data=json_data, headers=headers)
# response = requests.delete('http://127.0.0.1/delete-user/someTestUser', data=json_data, headers=headers)
# response = requests.get('http://127.0.0.1/delete-user/someTestUser')

# Print the response text (the content of the request)
print(response.text)