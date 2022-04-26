
# %%

def dec2bin(n: int):
    if n != 0:
        return dec2bin(n//2) * 10 + n % 2
    else:
        return 0


print(dec2bin(5))

# %%

def dec2bin2(n: int):
    result = []
    next=n
    while next!=0:
        result.append(str(next % 2))
        next //= 2
    result.reverse()
    return ''.join(result)

print(dec2bin2(5))

# %%

def fact_(n: int):
    s=1
    nn=n
    while nn != 1:
        s *= nn
        nn -= 1
    print(f'The factorial of {n} = {s}')

fact_(5)



# %%

def fact(n: int):
    s=n
    nn=n
    while nn > 1:
        s *= (nn -  1)
        nn -= 1
    print(f'The factorial of {n} = {s}')

fact(5)

# %%

class Customer:
    __logged_in = False

    #decorator function
    def is__logged_in(self, fn):
        def caller(self, *args, **kwargs):
            if self.__logged_in:
                return fn(self, *args, **kwargs)  # type: ignore
            else:
                print('You\'re not logged in.')
        return caller

    @is__logged_in  # type: ignore
    def book_trip(self):
        print('trip booked')


    def login(self, username, password):
        users= {
            'aaaaa': 'bbbbb',
            'ccccc': 'ddddd'
        }
        if username in users and users[username] == password:
            self.__logged_in = True
            print('[You\'re Logged In]'.center(100, '='))
            print('Welcome to Hell.'.center(100, ' '))
        else:
            print('Invalid Username or Password!')
    
    def logout(self):
        self.__logged_in = False
        print('[Logged out successfully]'.center(100, '='))

sudip = Customer()
sudip.book_trip()

sudip.login('aaaaa', 'sssss')
sudip.book_trip()

sudip.login('ccccc', 'ddddd')
sudip.book_trip()

sudip.logout()
sudip.book_trip()

# %%

add1=lambda a,b,:a+b
print(add1(1,2))
print(add1(4,4))