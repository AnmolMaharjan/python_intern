
# %%

a1 = int(input('a = '))
b1 = int(input('b = '))
if a1 > b1:
    print(f'{a1} is greater than {b1}')
    print(':)')
elif a1 < b1:
    print(f'{a1} is less than {b1}')
    print(':(')
else:
    print(':D')
print('-_-')

a1 = 22
b1 = 'even' if a1 % 3 == 0 else 'odd'
print(b1)