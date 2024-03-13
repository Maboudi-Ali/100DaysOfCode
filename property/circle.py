import math 

class Circle:

    def __init__(self, radius):
        self._radius = radius


    @property
    def radius(self):
        return self._radius

    
    @property.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('radius must be non-negative')
        else:
            self._radius = value


    @property
    def area(self):
        return self.radius ** 2 * math.pi


