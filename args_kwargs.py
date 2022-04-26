
# %%

def adds(*args):
    result = 0
    for element in args:
        result += element
    return result


print(adds(1, 2))
print(adds(1, 4, 2, 3, 4, 5, 6, 7, 8,  8, 9, 0, -3, 212, 435))
print(adds(*range(1, 1001)))

# %%

request = {
    'POST': {
        'first_name': 'Anmol1',
        'last_name': 'Maharjan',
        'license': '1123212',
    },

    'GET': {
        'first_name': 'Anmol2',
        'last_name': 'Maharjan',
        'license': '1123212',
    },
    'params': {
        'first_name': 'Anmol3',
        'last_name': 'Maharjan',
        'license': '1123212',
    },

    'headers': [

    ]
}

req = ['Susan', 'Maharjan', '123212']


def register_customer(first_name, last_name, license):
    print(
        f'The first name is {first_name} \nThe last name is {last_name} \nThe licence number is {license}')


register_customer(
    request['POST']['first_name'],
    request['POST']['last_name'],
    request['POST']['license'],
)

register_customer(**request['POST'])
register_customer(*req)

# %%


def register_customer_1(*args):
    pass

# %%


def register_customer_2(**kwargs):
    print(kwargs)


register_customer_2(**request['POST'])

# %%

adds(1, 2)
adds(1, 2, 3, 4)
adds(1, 2, 3, 4, 5, 6, 7, 8)


# %%

def print_detail(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: '{value}'")


print_detail(
    book_name='How to win friends and influence people. How to stop worrying and start living',
    price='$29.88',
    author='Dale Carnegie',
    co_author='Anmol Maharjan'
)

# %%


def add(a, b, c=0, *args, **kwargs):
    print('-'*100)
    print(f'a={a}')
    print(f'b={b}')
    print(f'c={c}')
    print(f'args={args}')
    print(f'kwargs={kwargs}')
    result = a+b+c
    for value in args:
        result += value
    for _, value in kwargs.items():
        result += value
    print(f'sum = {result}')


add(1, 2)
add(1, 2, 3)
add(1, 2, 3, 4)
add(1, 2, 3, 4, 5)
add(1, 2, 3, 4, 5, 6)
add(1, 2, 3, 4, 5, 6, m=7)
add(1, 2, 3, 4, 5, 6, m=7, n=8)
add(1, 2, 3, 4, 5, 6, m=7, n=8, o=9)

# %%

office = 10
home = 10
misc = [11, 22, 33, 44, 55]
other_exp = {
    'bus_fare': 100,
    'pen': 10,
    'gas': 20
}

add(office, home, 0, *misc, **other_exp)