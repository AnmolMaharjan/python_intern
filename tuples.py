
# %%

num=(11,23,44,67,13,34,56,21,61)
animals=('cat','dog','rat')
random=(55,'gate','sun','god,11.11')
print(animals)
for animal in animals:
    print(animal)

enum=enumerate(animals)
for(index, animals) in enum:
    print(f'{index}-{animals}') 

del num