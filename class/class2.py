class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year


    def get_info(self):
        return self.brand, self.model, self.year


