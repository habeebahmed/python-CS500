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
		
class Factory:
    def getMath(self):
        return PoorMath()
		
def main():
    math = Factory().getMath()
    print("Sum =", math.add())
	
if __name__ == '__main__':
    main()