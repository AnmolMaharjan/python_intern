from unicodedata import name


class Person:
    name = "Anmol"
    age = 58
    country = "Nepal"

x = getattr(Person, 'height', 'O Antava')
print(x)
