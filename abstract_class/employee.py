from abc import ABC, abstractmethod

class Employee(ABC):
    
    def __init__(self, name, age, base_salary):
        self.name = name
        self.age = age


    @asbtractmethod
    def calculate_salary(self):
        pass



class HourlyEmployee(Employee):

    def __init__(self, *args):
        super().__init__(self, *args)


    def calculate_salary(self, hours):
        return self.base_salary * hours


class SalariedEmployee(Employee):

    def __init(self, *args):
        super().__init__(self, *args)


    def calculate_salary(self):
        return self.base_salary



