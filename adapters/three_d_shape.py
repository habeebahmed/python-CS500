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
        
class ThreeDShape(ABC):
    @abstractmethod
    def getSurfaceArea(self):
        pass
        
    @abstractmethod
    def getTotalLength(self):
        pass
        
class RectangleSolid(ThreeDShape):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        
    def getSurfaceArea(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)
        
    def getTotalLength(self):
        return 4 * (self.length + self.width + self.height);
        
class ThreeDShapeAdapter(TwoDShape):
    def __init__(self, shape):
        self.shape = shape
        
    def getArea(self):
        return self.shape.getSurfaceArea() / 2
        
    def getPerimeter(self):
        return self.shape.getTotalLength() / 2

class Factory:
    def getShape(self, type):
        shape = None
        if type == "Rectangle":
            shape = Rectangle(80, 80)
        elif type == "RectangleSolid":
            shape2 = RectangleSolid(80, 80, 0)
            shape = ThreeDShapeAdapter(shape2)
      
        return shape
        
def main():
    type = input("Enter the shape type: ")
    shape = Factory().getShape(type)
    print("Area =", shape.getArea())
    print("Perimeter =", shape.getPerimeter())
    
if __name__ == '__main__':
    main()