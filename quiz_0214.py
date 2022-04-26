
# %%

person = {
    'name': 'Anmol',
    'age': 18,
    'profession' : 'Politician',
    'married': False
}
print(person.get('name'))
person['age']=10
print(person['age'])
print(f'{person}')

print(person['employed'])
# print(person.get('employed'))
print(person.get('employed', False))