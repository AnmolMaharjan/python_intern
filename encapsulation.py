
# %%

class MyClass:
    __value = 1

    def get_value(self):            #Getter Method
        return self.__value
    
    def set_value(self, value):     #Setter Method
        self.__value = value

class_1 = MyClass()
class_1.set_value(2)
print(class_1.get_value())
class_2 = MyClass()
class_2.set_value(5)
print(class_2.get_value())

# %%

MALE = 'male'
FEMALE = 'female'

class Student:
    def __init__(self, first_name, last_name, roll, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.roll = roll
        self.age  = age
        self.gender = gender
    
    # def full_name(self):
    #     return f"{self.first_name} {self.last_name}"

    def __lt__(self, other):
        return self.roll < other.roll

    def __str__(self) -> str:
        return f"{self.roll}\t{self.first_name} {self.last_name}\t\t{self.age}\t\t{self.gender}"

class ClassRoom:
    def __init__(self, name, class_teacher):
        self.__is_large = False
        self.__students = []
        self.name = name
        self.class_teacher = class_teacher

    def add_student(self, student: Student):
        print(f'Student {student.first_name} {student.last_name} is added successfully.')
        self.__students.append(student)
        if self.__students.__len__() > 3:
            self.__is_large = True
        else:
            self.__is_large = False
        
    def remove_student(self, student: Student):
        print(f'Student {student.first_name} {student.last_name} is removed successfully.')
        if student in self.__students:
            self.__students.remove(student)
            if self.__students.__len__() > 3:
                self.__is_large = True
            else:
                self.__is_large = False
        else:
            print(f"Student with name {student.first_name} {student.last_name} does not exist")

    def describe(self):
        print("Students")
        print('Roll\tName\t\t\tAge\t\tGenter')
        for student in sorted(self.__students):
            print(student)
        print("Large: ", self.__is_large)

class_9 = ClassRoom('Physics', 'Prof. Dr. Anmol Maharjan')

einstein = Student('Albert', 'Einstein', 2, 15, MALE)

class_9.add_student(einstein)

class_9.add_student(Student('Ada', 'Lovelace', 4, 15, FEMALE))
class_9.add_student(Student('Susan', 'Maharjan', 3, 15, MALE))
class_9.add_student(Student('Rajesh', 'Hamal', 1, 15, MALE))
class_9.add_student(Student('Archana', 'Paneru', 5, 15, FEMALE))

class_9.describe()

# %%

from typing import TypedDict

class Student1(TypedDict):
    name: str
    age: int

x: Student1={
    'age': 11,
    'name': 'Anmol',
}

xx: int = 5