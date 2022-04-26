
# %%

wild = [
    'tiger',
    'lion',
    'deer',
    'bear',
    'zebra'
]

print(wild)

wild.sort()
print(wild)

wild.reverse()
print(wild)

wild.append('leopard')
wild.append('elephant')
wild.append('rhino')
print(wild)

s=wild.index('leopard')
print(s)
wild.pop(s)
print(wild.index('leopard'))

wild.insert(2,'leopard')
print(wild)

wild.remove('rhino')
print(wild)