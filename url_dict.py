import re
url = 'https://www.345tool.com?name=test&roll=1&address=kathmandu&age=20'

# my_dict = {}
# x = re.findall(r'\?[\w&=]+', url)[0][1:].split('&')
# for i in x:
#     z = i.split('=')
#     my_dict[z[0]] = z[1]
# print(my_dict)

# y = [i.split('=') for i in x]
z = {a:b for a,b in [i.split('=') for i in re.findall(r'\?[\w&=]+', url)[0][1:].split('&')]}
print(z)
