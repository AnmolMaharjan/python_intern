
import re, json

with open('nile.csv', 'r') as fread:
    data = fread.read()

# %%

# my_dict = {}
# y=[]
# x = str.splitlines(data)

# for i in x:
#     y.append(re.split(r',',i))

# for i in range(1,len(y)):
#     my_dict[str(i)] = {}

# for i,(key,value) in enumerate(my_dict.items()):
#     for j in range(0,len(y[0])):
#         a = re.findall(r'\w+',y[0][j])
#         b = re.findall(r'[\w\.]+',y[i+1][j])
#         my_dict[key][a[0]] = b[0]

# with open('file_1.txt','w') as fwrite:
#     fwrite.write(json.dumps(my_dict))

# %%

my_dict = {}
y=[]
ff=[]
x = str.splitlines(data)

for i in x:
    y.append(re.split(r',',i))

for i in range(1,len(y)):
    ff.append(str(i))

for i,f in enumerate(ff):
    filename = 'file_' + f + '.txt'
    f = open(filename,'w')
    for j in range(0,len(y[0])):
        a = re.findall(r'\w+',y[0][j])
        b = re.findall(r'[\w\.]+',y[i+1][j])
        my_dict[a[0]] = b[0]
    f.write(json.dumps(my_dict))
    my_dict = {}
    f.close()
