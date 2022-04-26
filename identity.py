
# %%

# Identity operations
# - used to compare whether they are same object or not
# - they are not used to compare for equality
# - identity operators are:
#     1. `is`
#     2. `is not`

print(type('abc') is str)

l1 = ['abc', 'def']
l2 = l1
l3 = l1.copy()

print(l1)
print(l2)
print(l3)

print(l1 is l2)
print(l2 is l3)
print(l3 is l1)

print(l1 == l2)
print(l2 == l3)
print(l3 == l1)

x=[1,2,3,4,5]
y=x.copy()
y.pop()
print(x)
print(y)