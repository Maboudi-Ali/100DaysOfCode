class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __call__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_point = Point(new_x, new_y)
        return new_point

