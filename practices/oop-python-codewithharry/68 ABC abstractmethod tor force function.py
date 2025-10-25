from abc import ABC , abstractmethod
class Shape(ABC):

    @abstractmethod
    def printarea(self):
        return 0

class Ractangel(Shape):
    type = "Rectangel"
    sides = 4 

    def __init__(self): # constractor area function
        self.length = 6
        self.breadth = 7

    def printarea (self):
        return self.length + self.breadth
emp = Ractangel()