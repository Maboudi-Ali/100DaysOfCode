class Matrix:

    def __init__(self, lst):
        self.content = lst


    def __add__(self, other):
        r11 = self.content[0][0] + other.content[0][0]
        r12 = self.content[0][1] + other.content[0][1]
        r21 = self.content[1][0] + other.content[1][0]
        r22 = self.content[1][1] + other.content[1][1]
        return Matrix([[r11, r12], [r21, r22]])

    def __sub__(self, other):
        r11 = self.content[0][0] - other.content[0][0]
        r12 = self.content[0][1] - other.content[0][1]
        r21 = self.content[1][0] - other.content[1][0]
        r22 = self.content[1][1] - other.content[1][1]
        return Matrix([[r11, r12], [r21, r22]])


