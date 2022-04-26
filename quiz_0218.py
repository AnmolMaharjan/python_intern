
# %%

pi = 3.1415
print(f'{int(pi)}')

str_1 = '20'
str_2 = '30'

print(str_1 + str_2)
str_1 = int(str_1)
str_2 = int(str_2)
print(str_1 + str_2)

x = ['1', '2', '3', '4', '5']
sum = 0

for k in x:
    k = int(k)
    sum = sum + k
print(sum)

# %%

odd1 = [1,3,5,7,9,11,13,15]
prime1 = [2,3,5,7,11,13,17]
odd1 = set(odd1)
prime1 = set(prime1)
o=list(odd1-prime1)
p=list(prime1-odd1)
op=list(prime1-odd1 | odd1-prime1)
print(o)
print(op)
print(p)