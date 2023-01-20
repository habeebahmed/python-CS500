
from typing import Tuple


class MathOld:
    def divide(self, a: int, b: int) -> None:
        quotient = a // b
        remainder = a % b
        print("Quotient = ", quotient)
        print("Remainder = ", remainder)

class MathNew:
    def divide(self, a: int, b: int) -> Tuple[int, int]:
        quotient = a // b
        remainder = a % b
        return (quotient, remainder)


class MathAdapter(MathOld):
    def __init__(self, math: MathNew) -> None: # association with new
        self.__math = math()

    def divide(self, a: int, b: int) -> None: # inheritent on old
        quotient, remainder = self.__math.divide(a, b)
        print("Quotient = ", quotient)
        print("Remainder = ", remainder) 

def main():
    math = MathAdapter(MathNew)
    math.divide(5,6)


if __name__ == "__main__":
    main()
