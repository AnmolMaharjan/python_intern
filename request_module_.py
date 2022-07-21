import requests

url = 'https://www.youtube.com'
x = requests.get(url)
# print(x.status_code)
print(x.text)
