from abc import ABC, abstractmethod, abstractproperty

class IMath(ABC):
    @abstractmethod
    def add(self):
        pass
		
class PoorMath(ABC):
    def add(self):
        try:
            x = int(input("Enter the first integer: "))
            y = int(input("Enter the second integer: "))
        except ValueError:
            x = y = 0

        return x + y

class IMath2(ABC):
    @abstractmethod
    def add(self, x, y):
        pass
		
class GoodMath(ABC):
    def add(self, x, y):
        return x + y
        
class MathAdapter(IMath):
    def __init__(self, math):
        self.math = math
        
    def add(self):
        try:
            x = int(input("Enter the first integer: "))
            y = int(input("Enter the second integer: "))
        except ValueError:
            x = y = 0

        return self.math.add(x, y)

class Factory:
    def getMath(self):
        math = GoodMath()
        return MathAdapter(math)
		
def main():
    math = Factory().getMath()
    print("Sum =", math.add())
	
if __name__ == '__main__':
    main()