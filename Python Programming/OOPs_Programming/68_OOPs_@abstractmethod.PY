from abc import ABCMeta, abstractmethod #This is use to print some functions forcefully is defined in class method:

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0
    
class Rectangle(Shape):
    type = "Rectangle"
    side = 4
    def __init__(self) :
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.breadth*self.length
    
react1 = Rectangle()
print(react1.printarea())