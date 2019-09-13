import requests
# import os
#
# os.environ['HTTP_PROXY'] = url
# os.environ['HTTPS_PROXY'] = url

url = 'http://google.com'
response = requests.get(url)
print(response)
print()
print(response.status_code)
print()
print(response.headers)
print()
print(response.content)