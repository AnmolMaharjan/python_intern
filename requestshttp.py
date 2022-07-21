# %%

import requests
from requests.auth import HTTPBasicAuth

url = 'https://httpbin.org/cookies/set/sessioncookie/123456789'
verify = 'https://httpbin.org/cookies'

# request_delete1 = requests.delete(url)
# print(request_delete1.text)
# request_delete2 = requests.delete(url, allow_redirects=False)
# print(request_delete2.text)
# request_delete3 = requests.delete(url, auth=('user','pass'))
# print(request_delete3.status_code)
# request_delete4 = requests.delete(url, cert=('folder/myclient.cert'))
# print(request_delete4.status_code)
# request_delete5 = requests.delete(url, cookies={'favcolor':'red'})
# print(request_delete5.status_code)
# request_delete6 = requests.delete(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})
# print(request_delete6.status_code)
# request_delete7 = requests.delete(url, proxies = { "https" : "https://1.1.0.1:80"})
# print(request_delete7.status_code)
# request_delete8 = requests.delete(my_url, stream=True)
# print(request_delete8.status_code)
# request_delete9 = requests.delete(my_url, timeout=0.001)
# print(request_delete9.status_code)
# request_delete10 = requests.delete(my_url, verify='folder/tlscertificate')
# print(request_delete10.status_code)
# request_delete11 = requests.delete(my_url, verify=False)
# print(request_delete11.status_code)

# request_get1 = requests.get(url)
# print(request_get1.content)
# print(request_get1.text)
# print(request_get1)
# request_get2 = requests.get(url, params = {"model": "Mustang"})
# print(request_get2.text)
# request_get3 = requests.get(url, allow_redirects=False)
# print(request_get3.text)
# request_get4 = requests.get(url, auth=HTTPBasicAuth('user', 'pass'))
# print(request_get4.status_code)
# print(request_get4.text)
# print(request_get4.content)
# request_get5 = requests.get(url, cert=('folder/myclient.cert'))
# print(request_get5.status_code)
# request_get6 = requests.get(url, cookies={'favcolor':'red'})
# print(request_get6.status_code)
# request_get7 = requests.get(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})
# print(request_get7.status_code)
# request_get8 = requests.get(url, proxies = { "https" : "https://1.1.0.1:80"})
# print(request_get8.status_code)
# request_get9 = requests.get(my_url, stream=True)
# print(request_get9.status_code)
# request_get10 = requests.get(my_url, timeout=0.001)
# print(request_get10.status_code)
# request_get11 = requests.get(my_url, verify='folder/tlscertificate')
# print(request_get11.status_code)
# request_get12 = requests.get(my_url, verify=False)
# print(request_get12.status_code)

# request_head1 = requests.head(url)
# print(request_head1.text)
# request_head2 = requests.head(url, allow_redirects=True)
# print(request_head2.text)
# request_head3 = requests.head(url, allow_redirects=False)
# print(request_head3.text)
# request_head4 = requests.head(url, auth=('user','pass'))
# print(request_head4.status_code)
# request_head5 = requests.head(url, cert=('folder/myclient.cert'))
# print(request_head5.status_code)
# request_head6 = requests.head(url, cookies={'favcolor':'red'})
# print(request_head6.status_code)
# request_head7 = requests.head(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})
# print(request_head7.status_code)
# request_head8 = requests.head(url, proxies = { "https" : "https://1.1.0.1:80"})
# print(request_head8.status_code)
# request_head9 = requests.head(my_url, stream=True)
# print(request_head9.status_code)
# request_head10 = requests.head(my_url, timeout=0.001)
# print(request_head10.status_code)
# request_head11 = requests.head(my_url, verify='folder/tlscertificate')
# print(request_head11.status_code)

# request_patch = requests.patch(url)
# print(request_patch.text)

# request_post1 = requests.post(url)
# print(request_post1.text)
# request_post2 = requests.post(url, data = {'somekey': 'somevalue'})
# print(request_post2.text)
# request_post3 = requests.post(url, json = {'somekey': 'somevalue'})
# print(request_post3.text)
# request_post4 = requests.post(url, files = {'file': open('myfirstreact.png' ,'rb')})
# print(request_post4.text)
# request_post5 = requests.post(url, allow_redirects=False)
# print(request_post5.text)
# request_post6 = requests.post(url, auth=('user','pass'))
# print(request_post6.status_code)
# request_post7 = requests.post(url, cert=('folder/myclient.cert'))
# print(request_post7.status_code)
# request_post8 = requests.post(url, cookies={'favcolor':'red'})
# print(request_post8.status_code)
# request_post9 = requests.post(url, headers = {"HTTP_HOST": "MyVeryOwnHost"})
# print(request_post9.status_code)
# request_post10 = requests.post(url, proxies = { "https" : "https://1.1.0.1:80"})
# print(request_post10.status_code)
# request_post11 = requests.post(my_url, stream=True)
# print(request_post11.status_code)
# request_post12 = requests.post(my_url, timeout=0.001)
# print(request_post12.status_code)
# request_post13 = requests.post(my_url, verify='folder/tlscertificate')
# print(request_post13.status_code)
# request_post14 = requests.post(my_url, verify=False)
# print(request_post14.status_code)


# request_put = requests.put(url)
# print(request_put.text)

# request_request = requests.request(url)
# print(request_request.text)

s = requests.Session()
s.get(url)
r = s.get(verify)
print(r.text)
