
from cmath import pi
import math

# %% calculation

a = math.hypot(3,4) # 5

print(f'a = {a}')

# %% degree to radian

b = math.radians(90) # 1.5707963267948966

print(f'b = {b}')

# %% radian to degree

# c = math.degrees(π) # 180.0
c = math.degrees(pi) # 180.0
d = math.degrees(b) # 90.0

print(f'c = {c}')
print(f'd = {d}')

# %% sin, cos, tan, inverse, hyperbolic

e = math.sin(pi / 2)            # 1.0
print(f'e = {e}')

f = math.cos(pi / 2)            # 1.06.123233995736766e-17
print(f'f = {f}')

g = math.tan(pi / 2)            # 1.633123935319537e+16
print(f'g = {g}')

# hyperbolic functions
h = math.sinh(pi / 2)           # 2.3012989023072947
print(f'h = {h}')

i = math.cosh(pi / 2)           # 2.5091784786580567
print(f'i = {i}')

j = math.tanh(pi / 2)           # 0.9171523356672744
print(f'j = {j}')

# inverses
k = math.asin(1.0)              # 1.5707963267948966
print(f'k = {k}')

l = math.acos(1.0)              # 0.0
print(f'l = {l}')

m = math.atan(1.0)              # 0.7853981633974483
print(f'm = {m}')

# inverse hyperbolic functions
n = math.asinh(2.3)             # 1.570278543484978
print(f'n = {n}')

o = math.acosh(2.5)             # 1.566799236972411
print(f'o = {o}')

p = math.atanh(0.9)             # 1.4722194895832204
print(f'p = {p}')
