# Write a Python program to illustrate the concept of the Command method.

# Create several concrete classes of your choice. Each class must have at least one method as the core functionality. For example,

#     class Bird:

#     def fly(self):

#         print("A bird is flying in the sky")


# Create command classes to encapsulate the method invocation of these classes to illustrate the use of the command pattern.
# Create an Invoker class to connect these command objects
# Create a main method for testing your design.

from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> float:
        pass


class SUM:
    def __init__(self, a: float, b: float) -> None:
        self.__a: float = a
        self.__b: float = b

    def add_two_numbers(self) -> float:
        return self.__a + self.__b


class SUB:
    def __init__(self, a: float, b: float) -> None:
        self.__a: float = a
        self.__b: float = b

    def subtract_two_numbers(self) -> float:
        return self.__a - self.__b


class DIV:
    def __init__(self, a: float, b: float) -> None:
        self.__a: float = a
        self.__b: float = b

    def divide_two_numbers(self) -> float:
        return self.__a / self.__b


class MUL:
    def __init__(self, a: float, b: float) -> None:
        self.__a: float = a
        self.__b: float = b

    def multiply_two_numbers(self) -> float:
        return self.__a * self.__b


class ADD_OPERATION(Command):
    def __init__(self, add: SUM) -> None:
        self.__add = add

    def execute(self) -> float:
        return self.__add.add_two_numbers()


class SUB_OPERATION(Command):
    def __init__(self, sub: SUB) -> None:
        self.__sub = sub

    def execute(self) -> float:
        return self.__sub.subtract_two_numbers()


class DIVIDE_OPERATION(Command):
    def __init__(self, div: DIV) -> None:
        self.__div = div

    def execute(self) -> float:
        return self.__div.divide_two_numbers()


class MUL_OPERATION(Command):
    def __init__(self, mul: MUL) -> None:
        self.__mul = mul

    def execute(self) -> float:
        return self.__mul.multiply_two_numbers()


class Invoker:
    def __init__(self) -> None:
        self.__commands: list[Command] = []
        self.__result = 0

    def append_operation(self, command: Command) -> None:
        self.__commands.append(command)

    def execute_operations(self) -> None:
        for cmd in self.__commands:
            self.__result += cmd.execute()

    def print_result(self) -> None:
        print("The result of the operations is: ", self.__result)


def main():
    op1: ADD_OPERATION = ADD_OPERATION(SUM(5, 6))
    op2: MUL_OPERATION = MUL_OPERATION(MUL(6, 4))
    op3: DIVIDE_OPERATION = DIVIDE_OPERATION(DIV(10, 2))
    op4: SUB_OPERATION = SUB_OPERATION(SUB(14, 5))

    invoker: Invoker = Invoker()
    invoker.append_operation(op1)
    invoker.append_operation(op2)
    invoker.append_operation(op3)
    invoker.append_operation(op4)

    invoker.execute_operations()

    invoker.print_result()

if __name__ == "__main__":
    main()
