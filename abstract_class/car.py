from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def start(self):
        pass


    @abstractmethod
    def stop(self):
        pass


class SportsCar(Car):

    def __init(self, brand):
        self.brand = brand


    def start(self):
        pass


    def stop(self):
        pass


class Sedan(Car):
    
    def __init(self, brand):
        self.brand = brand


    def start(self):
        pass


    def stop(self):
        pass


