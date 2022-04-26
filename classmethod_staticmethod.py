
# %% 
class Animal:
    legs = 4

    def __init__(self):
        self.legs = 2

    @classmethod
    def leggs(cls):
        print('Total no. of legs: ', cls.legs)

    def leggs1(self):
        print('Total no. of legs: ', self.legs)

print(Animal.legs)

Animal.leggs()
Animal().leggs()

a=Animal()
# a.legs = 10
print(a.legs)
print(a.leggs())

# %%

class Length:
    cm = 2345
    @staticmethod
    def cm_to_m(value: float):
        return value/100
    
    @staticmethod
    def m_to_cm(value: float):
        return value*100
    
class Weight:
    @staticmethod
    def kg_to_lb(value: float):
        return value*2.20462
    
    def lb_to_kg(value: float):
        return value/2.20462

print(Length.cm_to_m(Length.cm))