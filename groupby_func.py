from itertools import groupby


animals = ['Bear', 'Donkey', 'Cat', 'Dog', 'Camel', 'Elephant']
animals = sorted(animals)
values = groupby(animals, lambda x: x[0])
grouped = {k: list(v) for k, v in values}
print(grouped)
