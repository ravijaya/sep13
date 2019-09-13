import requests
from pprint import pprint as pp

uri = 'https://reqres.in/api/users/82'

response = requests.get(uri)
print(response.status_code)
print()
pp(response.json())
