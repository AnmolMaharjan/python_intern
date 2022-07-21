import mymodule as a
import platform

a.greeting("anmol")

b = a.person1['age']
print(b)

c = platform.system()
print(c)

d = dir(platform)   # built-in function names
for i in d:
    print(i)
