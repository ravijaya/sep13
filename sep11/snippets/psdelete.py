import requests

uri = 'https://reqres.in/api/users/7'



response = requests.delete(uri)
print(response.status_code)
# print(response.text)

