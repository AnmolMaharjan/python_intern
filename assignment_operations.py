
# %%

# Assignment operations:
#     =
#     +=
#     -=
#     *=
#     /=
#     %=
#     //=
#     **=
#     &=
#     |=
#     ^=
#     >>=
#     <<=

from distutils.command import sdist
import numbers


x = 50
print(x)

x, y = 111, 10
print(f'x = {x} & y = {y}')

x += 2        # x = x + 2
print(x)

x -= 2          # x = x - 2
print(x)

x *= 2
print(x)

x &= 2
print(x)

x |= 2
print(x)

x ^= 2
print(x)

x >>= 2
print(x)

x <<= 2
print(x)

x /= 2
print(x)

x %= 2
print(x)

x //= 2
print(x)

x **= 2
print(x)