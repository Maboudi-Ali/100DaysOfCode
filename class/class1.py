class Rectangle:


    def __init__(self, width, length):
        self.width = width
        self.length = length

    
    def area(self):
        return self.width * self.length


    def perimeter(self):
        return 2 * (self.width + self.length)

