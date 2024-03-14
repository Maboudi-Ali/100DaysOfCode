class ComplexNumber:

    def __init__(self, r, i):
        self.r = r
        self.i = i


    def __str__(self):
        if self.i < 0:
            return f'{self.r} {self.i}i'
        elif self.i == 0:
            return self.r
        else:
            return f'{self.r} + {self.i}i'


    def __repr__(self):
        if self.i < 0:
            return f'{self.r} {self.i}i'
        elif self.i == 0:
            return self.r
        else:
            return f'{self.r} + {self.i}i'



    def __add__(self, other):
        new_r = self.r + other.r
        new_i = self.i + other.i
        return ComplexNumber(new_r, new_i)

    
    def __sub__(self, other):
        new_r = self.r - other.r
        new_i = self.i - other.i
        return ComplexNumber(new_r, new_i)


    def __mul__(self, other):
        new_r = self.r * other.r - self.i * other.i
        new_i = self.r * other.i + self.i * other.r
        return ComplexNumber(new_r, new_i)

