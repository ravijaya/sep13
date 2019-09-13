import requests
from json import loads
from pprint import pprint as pp


def create_user():
    """request to create user"""
    uri = 'http://127.0.0.1:5000/users'
    payload = dict(name='nickson3', ugroup='nickson3', email='nickson3@xyz.com')
    response = requests.post(uri, json=payload)
    print(response.status_code)
    print()
    print(response.json())


def request_using_urllib():
    import urllib.request
    with urllib.request.urlopen('http://127.0.0.1:5000/users/2') as f:
        print(f.headers)
        print()
        pp(loads(f.read().decode()))
        # print(dir(f))


def get_user_info(uri):
    response = requests.get(uri)
    print(response.status_code)
    print()
    print(response.headers)
    print()
    # print(response.text)
    # print(loads(response.text))
    # exit(1)
    print()
    content = response.json()
    print(content)
    print(type(content))


if __name__ == '__main__':
    # get_user_info('http://127.0.0.1:5000/users/2')
    # request_using_urllib()
    create_user()
    #print()
    #get_user_info('http://127.0.0.1:5000/users')
