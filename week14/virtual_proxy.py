
from abc import ABC, abstractmethod
import time
from threading import Thread

class MathInterface(ABC):
    @abstractmethod
    def getX(self):
        pass
        
    @abstractmethod
    def getY(self):
        pass
        
    @abstractmethod
    def getResult(self):
        pass
        
    @abstractmethod
    def process(self, x, y):
        pass
        
class MathReal(MathInterface):
    def __init__(self):
        self.__x = None
        self.__y = None
        self.__result = None
        
    def getX(self):
        return self.__x
        
    def getY(self):
        return self.__y
        
    def getResult(self):
        return self.__result
        
    def process(self, x, y):
        self.__x = x 
        self.__y = y 
        self.__result = x; 
        
        while y > 0: 
            self.__result *= x
            y -= 1
            time.sleep(1)
        
class MathProxy(MathInterface):
    def __init__(self):
        self.__inProgress = False
        self.__math = None
        
    def getX(self):
        if self.__main is None:
            return 0
        else:
            return self.__math.getX()
        
    def getY(self):
        if self.__main is None:
            return 0
        else:
            return self.__math.getY()
        
    def getResult(self):
        if self.__math is None:
            return 0
        else:
            return self.__math.getResult()
        
    def process(self, x, y):
        print("Processing, please wait...")
        self.__inProgress = True
        
        def execute(x, y):
            temp = MathReal()
            temp.process(x, y)
            self.__math = temp
            
        t = Thread(target=execute, args=(x,y,))
        t.start()
        
def main():
    result = 0
    math = MathProxy()
    
    while result == 0:
        math.process(2, 10)
        result = math.getResult()
        time.sleep(1)

    print('The result is ', result)
    
    
main()