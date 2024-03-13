from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    
    @abstractmethod
    def greet(self):
        pass


    @abstractmethod
    def introduce(self):
        pass


class Teacher(Person):

    def __init__(self, name, age):
        super().__init__(name, age, 'Teacher')


    def greet(self):
        print('Hi Students')


    def introduce(self):
        print(f'I am {name}, your new teacher')


class Student(Person):

    def __init__(self, name, age):
        super().__init__(name, age, 'Student')


    def greet(self):
        print('Hello Teacher')


    def introduce(self):
        print(f'I am {name}, student of this class')


