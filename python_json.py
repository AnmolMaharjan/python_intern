import json

x = '{"name":"Anmol", "age":100, "city":"Yala"}'
y = json.loads(x)
print(y['age'])
print(y['city'])
a = {
    "name":"Anmol",
    "age":100,
    "city":"Yala",
    }
z = json.dumps(a, indent=5, separators=('. ', '= '), sort_keys=True)
print(z)
