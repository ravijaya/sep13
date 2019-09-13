import requests

uri = 'http://127.0.0.1:5000/api/tasks/9'
response = requests.delete(uri)
print(response.status_code)
print(response.content)