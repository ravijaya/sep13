import requests

uri = 'https://reqres.in/api/users/365'


payload = {
    "name": "james oliver",
    "job": "supervisor"
}

response = requests.put(uri, json=payload)
print(response.json())

