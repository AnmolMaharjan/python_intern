
import os
# import pickle

# def add_function(a, b):
#     '''Takes two numbers a & b,returns sum of a & b.'''
#     return a+b
# def add_sum(a, b):
#     '''Returns sum of two numbers:
#     Parameters:
#     a (int): A decimal integer
#     b (int): A decimal integer
#     Returns:
#     Integer sum of a & b'''
#     return a+b

class Person(object):
     """
    A class to represent a person.

    ...

    Attributes
    ----------
    name : str
        first name of the person
    surname : str
        family name of the person
    age : int
        age of the person

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """

def __init__(self, name, surname, age):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            name : str
                first name of the person
            surname : str
                family name of the person
            age : int
                age of the person
        """

        self.name = name
        self.surname = surname
        self.age = age

def info(self, additional=""):
        """
        Prints the person's name and age.

        If the argument 'additional' is passed, then it is appended after the main info.

        Parameters
        ----------
        additional : str, optional
            More info to be displayed (default is None)

        Returns
        -------
        None
        """
        print(f'My name is {self.name} {self.surname}. I am {self.age} years old.' + additional)

os.system('cls' if os.name == 'nt' else 'clear')

# print("-"*40)
# print(add_function.__doc__)      # Single-line docstrings
# print("-"*40)
# print(print.__doc__)            # Docstrings for the built-in print() function
# print("-"*40)
# print(pickle.__doc__)           # Docstrings for the built-in print() function
# print("-"*40)
# print(add_sum.__doc__)          # Docstrings for Python functions
# print("-"*40)
# print(Person.__doc__)
help(Person)
