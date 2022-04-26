
# %% 

m = [1, 2, 3, 4, 5]
n = [6, 7, 8, 9, 10]


def dd(a):
    return a**2


x = map(dd, m)
y = map(dd, n)
print(list(x))
print(list(y))

x = map(lambda x: dd(x), m)
print(list(x))