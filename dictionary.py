
# %%

person = {
    'name': 'Trump',
    'age': 60,
    'relationship': 'divorced',
    'position': ['manager', 'politician']
}
print(person['name'])
print(person['age'])
print(person['relationship'])
print(person['position'])

print(person.get('name'))
print(person.get('middle_name'))
print(person.get('age'))
print(person.get('relationship'))
print(person.get('position'))
print(person.get('father', False))
print(person.get('age', False))
print(person.get('occupation', 'officer'))
print(person.get('name', 'modi'))
print(person.__len__())
print(len(person))



person['gender'] = 'male'
person['occupation'] = 'beggar'
person['middle_name'] = 'john'

print(person)
other_fields = {
    'age': 61,
    'origin': 'alien',
    'species': 'not-identified',
    'affiliation': 'bs'
}
person.update(other_fields)
print(person.pop('occupation'))
print(person)

popped_item = person.pop('gender')
print(popped_item)
print(person)

s = person.popitem()
print(person)
print(s)

(aa, bb) = person.popitem()
(_, c) = person.popitem()
(d, _) = person.popitem()
(_, _) = person.popitem()
print(aa, bb)
print((c))
print((d, _))
print((_, _))

tuple_1 = person.popitem()
for key in person:
    print(f'The key is {key}')

for key in person:
    print(f'The {key} is {person[key]}')

for value in person.values():
    print(f'The value is {value}')

for (key, value) in person.items():
    print(f'The {key} is {value}')