import requests
from pprint import  pprint as pp

credit = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

s = requests.session()
response = s.post('https://reqres.in/api/login', json=credit)
pp(response.json())
