import enum

class ComputerType(enum.Enum):
    Computer = 1
    SuperComputer = 2
    UltraComputer = 3


class Computer:
    def __init__(self, cpu: int) -> None:
        self.__cpu = cpu

    def compute(self):
        print("The computer is solving a problem.")

class SuperComputer(Computer):
    def __init__(self, cpu: int) -> None:
        super().__init__(cpu)

    def compute(self):
        super().compute()
        print("The computer is running a simulation.")

class UltraComputer(SuperComputer):
    def __init__(self, cpu: int) -> None:
        super().__init__(cpu)

    def compute(self):
        super().compute()
        print("The computer is running a 3-D modeling.")



class ComputerFactory:
    def create_computer(self, type: ComputerType, cpu: str):
        if type == ComputerType.Computer:
            c = Computer(cpu)
        elif type == ComputerType.SuperComputer:
            c = SuperComputer(cpu)
        elif type == ComputerType.UltraComputer:
            c = UltraComputer(cpu)
        
        return c