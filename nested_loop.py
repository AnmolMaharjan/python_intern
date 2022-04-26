
# %%

from distutils.command import sdist


s4 = [1, 3, 5, 7, 9, 11, 13, 15]

t1 = s4.index(5)
t2 = s4.index(7)

if t1 < t2:
    sd = [*s4[:t1], *s4[t2 + 1:]]
print(sdist)

# %%

# 1
# 1  2
# 1  2  3
# 1  2  3  4
# 1  2  3  4  5

for a4 in range(2, 7):
    for b in range(1, a4):
        print(b, end='  ')
    print()

# %%

# 1
# 1  2
# 1  2  3
# 1  2  3  4
# 1  2  3  4  5

for x in range(1, 6):
    print(''.join([str(y) for y in range(1, x+1)]))

# %%

# 1  2  3  4  5
# 1  2  3  4  5
# 1  2  3  4  5
# 1  2  3  4  5
# 1  2  3  4  5

for a5 in range(1, 6):
    for b in range(1, 6):
        print(b, end='  ')
    print('')

# %%

# 1  2  3  4  5
# 2  4  6  8  10
# 3  6  9  12  15
# 4  8  12  16  20
# 5  10  15  20  25

for a6 in range(1, 6):
    for b in range(1, 6):
        print(b*a6, end='  ')
    print('')

# %%

# 1  2  3  4  5
# 1  4  9  16  25
# 1  8  27  64  125
# 1  16  81  256  625
# 1  32  243  1024  3125

for a7 in range(1, 6):
    for b in range(1, 6):
        print(b**a7, end='  ')
    print('')

# %%

# 1
# 2  2
# 3  3  3
# 4  4  4  4
# 5  5  5  5  5

for a8 in range(1, 6):
    for b in range(1, a8+1):
        print(a8, end='  ')
    print('')

# %%

# 5
# 5  4
# 5  4  3
# 5  4  3  2
# 5  4  3  2  1

for a9 in range(1, 6):
    for b in range(1, a9+1):
        print(6-b, end='  ')
    print('')

# %%

# 5  4  3  2  1
# 5  4  3  2
# 5  4  3
# 5  4
# 5

for a10 in range(1, 6):
    for b in range(5, a10-1, -1):
        print(b, end='  ')
    print('')

# %%

#                1
#             1  2
#          1  2  3
#       1  2  3  4
#    1  2  3  4  5

for a11 in range(1, 6):
    for b in range(5, a11-1, -1):
        print(' ', end='  ')
    for b in range(1, a11+1):
        print(b, end='  ')
    print('')

# %%

#                1
#             1  2  1
#          1  2  3  2  1
#       1  2  3  4  3  2  1
#    1  2  3  4  5  4  3  2  1

for a12 in range(1, 6):
    for b in range(5, a12-1, -1):
        print(' ', end='  ')
    for b in range(1, a12+1):
        print(b, end='  ')
    for b in range(a12-1, 0, -1):
        print(b, end='  ')
    print('')

# %%

#              1
#           1  2  3
#        1  2  3  4  5
#     1  2  3  4  5  6  7
#  1  2  3  4  5  6  7  8  9

for a13 in range(1, 6):
    print('   '*(6-a13), end='  ')
    for b in range(1, 2*a13):
        print(b, end='  ')
    print('')

# %%


#                    1
#                1   2   3
#            1   2   3   4   5
#        1   2   3   4   5   6   7
#    1   2   3   4   5   6   7   8   9

for a13 in range(1, 12, 2):
    print('  ' * (12-a13), end=' ')
    for b in range(1, a13-1):
        print(b, end='   ')
    print('')