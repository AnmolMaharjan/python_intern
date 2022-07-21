
import requests

url = "http://172.16.10.13:8000/api/jobs/hrog/"

res = requests.head(url)
print(res.headers)
