
# %%

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = []
for x in numbers:
    result.append(x ** 2)

result = [x**2 for x in range(1, 11)]
print(result)

# %%


x = [1, 2, 3, 4, 5]
y = []

z = [a**2 for a in x]
print(z)

# for a in x:
#     y.append(a**2)
# print(y)

# %%

x = [1, 2, 3, 4, 5]
y = []

z = [a**3 for a in x]
print(z)

# %%

y = [2*x+1 for x in range(10)]
print(y)

# %%

y = {k: k**2 for k in range(10)}
print(y)

z = {}
for k in range(1, 11):
    z[k] = k**2
print(z)

# %%

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y = [y for y in x if y % 2 == 0]
print(y)

# %%

a14 = []
for x in range(1, 4):
    b = []
    for y in range(1, 4):
        b.append(y)
    a14.append(b)
print(a14)

# %%


a15 = []
for x in range(1, 4):
    # b=[y for y in range(1,4)]
    a15.append([y for y in range(1, 4)])
print(a15)

# %%

a16 = [[y for y in range(1, 4)] for x in range(1, 4)]
print(a16)

# %%

a17 = []
for x in range(1, 3):
    b = []
    for y in range(1, 3):
        c = []
        for z in range(1, 3):
            c.append(z)
        b.append(c)
    a17.append(b)
print(a17)

# %%

a18 = [[[z for z in range(1, 3)] for y in range(1, 3)] for x in range(1, 3)]
print(a18)