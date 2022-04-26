
# %%

aa = {2, 4, 6, 8, 10}
bb = {2, 3, 5, 7}
print(aa.union(bb))
print(aa.intersection(bb))
print(bb.intersection(aa))
print(aa.difference(bb))
print(aa.symmetric_difference(bb))
print(aa | bb)  # union -> pipe(|)
print(aa & bb)  # intersection -> ampersand(&)
print(aa - bb)  # diffference -> hyphen(-)
print(aa ^ bb)  # symmetric difference -> carat(^)

a = set(range(0, 12))
b = set(range(5, 13))
print(a)
print(b)