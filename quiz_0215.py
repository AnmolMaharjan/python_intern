
# %%

car = {
    'brand': 'Rolls Royce',
    'model': 'Phantom',
    'price': 6563600
}

car_ = {
    'color': 'Black',
    'no_of_seats': 5,
    'transmission': 'Automatic'
}

car.update(car_)

del car['color']
print(car)
car.popitem()
print(car)

for k in car:
    print(f'The key is {k}')

for k in car.keys():
    print(f'The key using keys() is {k}')

for v in car.values():
    print(f'The value using values is {v}')

for (k,v) in car.items():
    print(f'The {k} is {v}')