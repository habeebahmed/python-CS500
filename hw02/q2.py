# Design a class named MyInteger. The class contains:
#     ● An int data attribute named value that stores the int value represented by this object.
#     ● A constructor that creates a MyInteger object for the specified int value.
#     ● A getter method that returns the int value.
#     ● A setter method that sets the int value.
#     ● The methods iseven(self), isodd(self), and isprime(self) that return true if the value in self object is
#     even, odd, or prime, respectively.
#     ● The __eq__(self, other : MyInteger) that returns true if the value in the self object is equal to the value
#     of the other object.
#     ● The __str__(self) that returns the string representation of the object.
#     ● The add(self, other : MyInteger) that adds the value of the other object to the value of the self object.
#     ● The sub(self, other : MyInteger) that subtracts the value of the other object from the value of the self
#     object
#     ● The __gt__(self, other: MyInteger) that is the implementation of > operator. If the value of the self object
#     is greater than thevalue of the other object, it returns true otherwise false.
#     ● Draw the UML diagram for the class and then implement the class. Write a client program that tests all
#     methods in the class.

from __future__ import annotations


class MyInteger:
    def __init__(self, value: int) -> None:
        self.__value: int = value

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int) -> None:
        self.__value = value

    def iseven(self) -> bool:
        return bool(self.value and self.value % 2 == 0)

    def isodd(self) -> bool:
        return bool(self.value and self.value % 2 == 1)

    def isprime(self) -> bool:
        '''
            Validate if a number is prime or not
        '''
        count: int = 0
        if self.value == 1:
            return False
        for x in range(1, int(self.value/2 + 1)):
            if self.value % x == 0:
                count += 1
        return False if count >= 2 else True

    def __eq__(self, other: MyInteger) -> bool:
        return bool(self.value == other.value)

    def __str__(self) -> str:
        return ""+str(self.value)

    def add(self, other: MyInteger) -> None:
        if self.value:
            self.value += other.value

    def sub(self, other: MyInteger) -> None:
        if self.value:
            self.value -= other.value

    def __gt__(self, other: MyInteger) -> bool:
        return bool(self.value and other.value and self.value > other.value)


def main() -> None:
    int1: MyInteger = MyInteger(7)
    int2: MyInteger = MyInteger(10)
    int3: MyInteger = MyInteger(5)
    print("Is even: ", str(int1.iseven()))
    print("Is odd: ", str(int1.isodd()))
    print("Is prime: ", str(int1.isprime()))

    if (int1 == int2):
        print("both numbers are equal")

    print("Integer 1 is", int1)
    print("Integer 2 is", int2)

    int1.add(int3)
    print("result after adding {} is {}".format(int3, int1))

    int1.sub(int3)
    print("Integer after subtracting {} is {}".format(int3, int1))

    if (int1 > int3):
        print("Integer {} is greater than {}".format(int1, int3))


if __name__ == "__main__":
    main()
