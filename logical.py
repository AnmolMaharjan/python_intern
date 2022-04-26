
# %%

print(True and True)        # True
print(True and False)       # False
print(False and True)       # False
print(False and False)      # False

print(True or True)        # True
print(True or False)       # True
print(False or True)       # True
print(False or False)      # False

print(not True)     # False
print(not False)    # True

cloudy = False
rained = True

rains = cloudy and rained

if rains:
    print("it rains today")
else:
    print("It does not rain today")