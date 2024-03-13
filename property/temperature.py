class Temperature:

    def __init__(self, temp):
        self._temp = temp


    @property
    def centigrade(self):
        return self._temp


    @property
    def fahrenheit(self):
        return self.centigrade * 9 / 5 + 32


