
# %%

x = 0
while x >= 0:
    x += 1
    print(x)
    if x == 5:
        continue
    if x == 11:
        break

x = 1
while x != 1:
    x += 1
    print('while')
else:
    x -= 1
    print('else')

a2 = 2
while a2 >= 2:
    a2 -= 1
    print('a2>=2')
    while a2 <= 2:
        a2 += 1
        print('a2<=1')
        continue