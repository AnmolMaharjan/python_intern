import json
import requests

base_url = 'http://172.16.10.26:8001'
# %%

# url = f"{base_url}/api/user/login/"

# data = {
#   "email": "admin@ewebsign.com",
#   "password": "admin123`$"
# }

# response_post = requests.post(url, json = data)
# print(json.dumps(response_post.json(), indent=4))

# %%

url = f"{base_url}/api/jobs/hrog/"
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyMDc3NjcwLCJpYXQiOjE2NTIwNzc0OTAsImp0aSI6IjI0MDllNGIzZDMyZDQxYzlhMmI2NTY5ZDE4NjYzNjJiIiwidXNlcl9pZCI6Mn0.So_4Hmn19mfddiBIP4oB0MmPF9SsB0nh0lbibMd5X_M"
refresh_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NDY2OTQ5MCwiaWF0IjoxNjUyMDc3NDkwLCJqdGkiOiJjODM1MzUxMjVkMzU0NmU2YTRkMWQwNTA0YTY4NzNmNCIsInVzZXJfaWQiOjJ9.q3I3gG-DQ_MyinB10l5UMEgQ2QxZgyNTQvSVkXtQG9g"
res = requests.get(url, headers={'Authorization': f'Bearer {access_token}'})

with open('api_fetch.json', 'r+',encoding='UTF-8') as file:
    aa = json.dumps(res.json(), indent=4, ensure_ascii=False)
    file.write(aa)
    print(aa)

# %%

# import requests

# url = "http://172.16.10.13:8000/api/jobs/hrog/"

# res = requests.head(url)
# xx=res.headers

# for (i,j) in xx.items():
#     print(f'{i} : {j}')
