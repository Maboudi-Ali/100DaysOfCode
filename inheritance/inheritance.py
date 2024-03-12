class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species

    
    def make_sound():
        print('Generic aminal sound')



class Mammal(Animal):

    def __init__(self, name, species, leg_num):
        super().__init__(name, species)
        self.leg_num = leg_num


    def make_sound():
        print('Generic mammal sound')



class Dog(Mammal):

    def __init__(self, name, species, leg_num, breed):
        super().__init__(name, species, leg_num)
        self.breed = breed

    
    def make_sound():
        print('Woof!')

