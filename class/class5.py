class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def increase_salary(self, amount):
        self.salary += amount


    def show_info(self):
        return self.name, self.salary



