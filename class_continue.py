
# %%

class Animal:
    legs = 4

    @classmethod    # bound to the class so class is passed as the first argument instead of self
    def print_legs(cls):
        print('Total no. of legs: ', cls.legs)

    # Regular method that is bound to the instance so self is passed as the first argument
    def print_legs_1(self):
        print('Total no. of legs: ', self.legs)

    @staticmethod
    # Regular method that is bound to the instance so self is passed as the first argument
    def print_legs_2(legs):
        print('Total no. of legs: ', legs)


zebra = Animal()
zebra.print_legs()

zebra.legs = 2
zebra.print_legs()
print(zebra.legs)

zebra.print_legs_2(4)