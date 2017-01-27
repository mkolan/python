
class Vehicle:

    def __init__(self, name, colour):
        self.__name = name
        self.__colour = colour

    def getColour(self):
        return self.__colour

    def setColour(self, colour):
        self.__colour = colour

    def getName(self):
        return self.__name

class Car(Vehicle):
    def __init__(self, name, colour, model):
        super().__init__(name,colour)
        self.__model = model

    def getDescription(self):
        return self.getName() + self.__model + self.getColour()

c = Car("honda", "red", "2013")
print (c.getDescription())
print(c.getName())