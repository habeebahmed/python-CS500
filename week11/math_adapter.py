from abc import ABC, abstractmethod
from re import I


class IMath(ABC):
    @abstractmethod
    def add(self, a, b):
        pass
class Math(IMath):
    def add(self, a, b):
        return a + b

class IMath2(ABC):
    @abstractmethod
    def add(self, a, b, c):
        pass

class Math2(IMath2):
    def add(self, a, b, c):
        return a+b+c

class MathAdapter(IMath):
    def __init__(self) -> None:
        self.__math = Math2()
    def add(self, a, b):
        return self.__math.add(a,b,0)

class Factory:
    def get_math(self):
        return MathAdapter()

########################################################################


# Client's program
def main():
    m = Factory().get_math()
    print(m.add(5, 6))


main()