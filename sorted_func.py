print(sorted([1,3,5,7,9,2,4,6,8,0]))
print(sorted([1,3,5,7,9,2,4,6,8,0], reverse = True))
person = {
    'name': 'Anmol Maharjan',
    'age': 18,
    'occupation': 'python-developer'
}
print(sorted(person))
print(sorted(person.items()))
print({k:v for k,v in sorted(person.items())})

students = [
    ('A',1),
    ('B',2),
    ('C',3),
    ('D',4),
    ('E',5)
]
print(sorted(students, key=lambda x: x[1]))
