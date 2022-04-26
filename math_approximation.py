
# %% round function

import math


x = round(5.49)         # 5
y = round(5.50)         # 6
z = round(5.51)         # 6

a = round(9.87654, 3)   # 9,877

print(f'x = {x}')
print(f'y = {y}')
print(f'z = {z}')

print(f'a = {a}')

# %% floor function The floor() function returns the largest integer that is less than or equal to the provided number. The floor() function takes only one argument and returns the integer value.

b = math.floor(5.49)    # 5
c = math.floor(-5.49)   # -6
d = math.floor(5.50)    # 5
e = math.floor(-5.50)   # -6
f = math.floor(5.51)    # 5
g = math.floor(-5.51)   # -6

print(f'b = {b}')
print(f'c = {c}')
print(f'd = {d}')
print(f'e = {e}')
print(f'f = {f}')
print(f'g = {g}')

# %% ceil function

h = math.ceil(5.49)     # 6
i = math.ceil(-5.49)    # -5
j = math.ceil(5.50)     # 6
k = math.ceil(-5.50)    # -5
l = math.ceil(5.51)     # 6
m = math.ceil(-5.51)    # -5

print(f'h = {h}')
print(f'i = {i}')
print(f'j = {j}')
print(f'k = {k}')
print(f'l = {l}')
print(f'm = {m}')

# %% trunc function

n = math.trunc(5.49)    # 5
o = math.trunc(-5.49)   # -5

print(f'n = {n}')
print(f'o = {o}')
