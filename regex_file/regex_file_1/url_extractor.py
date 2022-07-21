
import re

with open('url.txt','r') as f_read:
    url = f_read.read()

x = re.findall(r'https?://[\w.-]+',url)

with open('domain.txt','w') as f_write:
    f_write.write('\n\n'.join(x))
