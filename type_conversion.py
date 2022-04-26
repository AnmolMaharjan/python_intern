
# %%

x5 = 5
y5 = 11.11
print(x5+y5)

# %%

x4 = 5
x4 = str(5)
print(type(x4))

# %%

x3 = '55'
x3 = int(55)
print(type(x3))

# %%

pi = 3.1415
pi = int(float(3.1415))
print(type(pi))

# %%

pi = '3.1415'
if pi.isdigit():
    pi = int(pi)
else:
    pi = float(pi)
print(type(pi))

# %%

x2=[1.2,2.3,3.4,4.5,5.6,6.7,7.8,8.9,9.10,0.1]

#no type casting
result = 0
for a1 in x2:
    result = result + int(a1)
print(result)

#type casting in loop
r=0
for b1 in x2:
    r=r+int(b1)
print(r)

#type casting in result
r2=0
for c1 in x2:
    r2=r2 + int(c1)
print(int(r2))

x2=list(set(x2))
print(x2)