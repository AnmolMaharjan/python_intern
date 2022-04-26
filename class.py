
# %% 
class person:
    first_name = '',
    last_name = '',
    address = '',
    city = '',
    age = 0

    def show_fullname(self):
        print(f"{self.first_name} {self.last_name}")

usopp = person()

usopp.first_name = 'Usopp'
usopp.last_name = 'Sogeking'
usopp.address='Syrup Village'
usopp.city='Gecko Island'
usopp.age=19

print(usopp.first_name)

usopp.show_fullname()


# %%

class Animal:
    name = ''
    paws = 0
    word = ''

    def __init__(self, name, word):
        self.name = name
        self.word = word

    def __str__(self):
        return f'Instance of Animal named {self.word}'
    
    def speak(self):
        print(f'I am {self.name} and i speak with {self.word}s.')

    def rename(self, new_name):
        self.name = new_name

reindeer = Animal('chopper', 'luffy')

reindeer.speak()
reindeer.rename('Tony Tony Chopper')
reindeer.speak()

khicha = Animal('puppy','hwauhwau')
khicha.speak()
