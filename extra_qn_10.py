
import re

x = [
    "0x4567",
    "0xA002",
    "AA47",
    'Ag42',
    "521044",
    "55ff",
    "55gg",
    "0x9876",
    "0xAg4f",
    "0xqrst",
    "0x455D"
]

y=[]
for i in x:
    # b = re.match(r"^(0x)?[A-Fa-f0-9]+$", i)
    # if b: y.append(b.group())
    if re.match(r"^(0x)?[A-Fa-f0-9]+$", i):
        y.append(i)
y=[i for i in x if re.match(r"^(0x)?[A-Fa-f0-9]+$", i)]
print(y)

x=0x55
print(x)

a = 'abababababababbabaababababab'
print(re.findall(r'[ab]{3,6}?',a))
