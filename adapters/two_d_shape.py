from abc import ABC, abstractmethod, abstractproperty

class TwoDShape(ABC):
    @abstractmethod
    def getArea(self):
        pass
        
    @abstractmethod
    def getPerimeter(self):
        pass
        
class Rectangle(TwoDShape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def getArea(self):
        return self.length * self.width
        
    def getPerimeter(self):
        return 2 * (self.length + self.width)
        
class Factory:
    def getShape(self, type):
        shape = None
        if type == "Rectangle":
            shape = Rectangle(80, 80)
            
        return shape
        
def main():
    type = input("Enter the shape type: ")
    shape = Factory().getShape(type)
    print("Area =", shape.getArea())
    print("Perimeter =", shape.getPerimeter())
    
if __name__ == '__main__':
    main()