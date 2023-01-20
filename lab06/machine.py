from abc import ABC, abstractmethod
from typing import Dict, List


class Movable(ABC):
    @abstractmethod
    def move(self) -> None:
        pass

class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass

class Flayable(ABC):
    @abstractmethod
    def fly(self) -> None:
        pass

class Part(Displayable):
    def __init__(self, partno: int, price: float) -> None:
        self.__partno: int = partno
        self.__price: float = price
    
    @property
    def partno(self):
        return self.__partno
    
    @property
    def price(self):
        return self.__price

    def display(self) -> None:
        print(f"partno = {self.__partno}")
        print(f"price = {self.__price}")

class JetFighter(Flayable, Displayable):
    def __init__(self, model: str, speed: int) -> None:
        self.__model: str = model
        self.__speed: int = speed
    
    def fly(self) -> None:
        print(f"The JetFigher {self.__model} is flying in the sky!")

    def display(self) -> None:
        print(f"model = {self.__model}")
        print(f"speed = {self.__speed}")

class MovablePart(Part):
    def __init__(self, partno: int, price: float, type: str) -> None:
        super().__init__(partno, price)
        self.__type: str = type

    @property
    def type(self):
        return self.__type

    def display(self) -> None:
        super().display()
        print(f"Type: {self.__type}")

    def move(self) -> None:
        print(f"partno: {self.partno} is moving fast!")


# No need to add ABC because displayable is already abstract
class Machine(Displayable):
    def __init__(self, machine_name: str ) -> None:
        self.__machine_name = machine_name
        self.__parts: List[Part] = []

    @property
    def machine_name(self):
        return self.__machine_name
    @property
    def parts(self) -> List[Part]:
        return self.__parts

    @abstractmethod # if None = 0 in class diagram then it's abstract method
    def dowork(self) -> None:
        pass

    def add_part(self, part: Part) -> None:
        self.__parts.append(part)
    
    def display(self) -> None:
        print(f"Machine name {self.__machine_name}")
        print("The machine has these parts:")
        for part in self.__parts:
            part.display()
            print()

    def remove_part(self, partno: int):
        index: int = next((index for (index, d) in enumerate(
            self.__parts) if d.partno == partno), -1)
        if index != -1:
            self.__parts.pop(index)
    
    def find_duplicated_parts(self)-> Dict[int, int]:
        duplicate_parts: dict[int, int] = {}
        for part in self.__parts:
            if (part.partno not in duplicate_parts):
                duplicate_parts[part.partno] = 1
            else:
                duplicate_parts[part.partno] += 1

        return dict(filter(lambda elem: elem[1] > 1, duplicate_parts.items()))

class Robot(Machine, JetFighter):
    def __init__(self, machine_name: str, cpu: str, model: str, speed: int) -> None:
        Machine.__init__(self, machine_name)
        JetFighter.__init__(self, model, speed)
        self.__cpu = cpu
    
    def dowork(self) -> None:
        print(f"The Robot {self.machine_name} is assembling a big truck.")
    
    def fly(self) -> None:
        JetFighter.fly(self)
        print(f"The Robot {self.__cpu} is flying over the ocean!")

    def display(self) -> None:
        print("cpu =", self.__cpu)
        Machine.display(self)
        JetFighter.display(self)

    # get list of parts whose prices are more than priceLimit
    def get_expensive_parts(self, priceLimit: float) -> List[Part]:
        return list(filter(lambda x: x.price > priceLimit, self.parts))

    def get_movable_parts_bytype(self) -> Dict[str, List[Part]]:
        movable_parts_group: dict[str, List[Part]] = {}
        for part in self.parts:
            if isinstance(part, MovablePart):
                if part.type not in movable_parts_group:
                    movable_parts_group[part.type] = [part]
                else:
                    movable_parts_group[part.type].append(part)

        return movable_parts_group
    
    def get_movable_parts(self) -> List[MovablePart]:
        movable_parts: List[MovablePart] = []
        for part in self.parts:
            if isinstance(part, MovablePart):
                movable_parts.append(part)
        
        return movable_parts
    
def main():
    robo = Robot('MTX', 'M1X', 'F-16', 10000)
    robo.add_part(Part(111, 100))
    robo.add_part(Part(222, 200))
    robo.add_part(Part(333, 300))
    robo.add_part(Part(222, 300))
    robo.add_part(MovablePart(555, 300, "TypeA"))
    robo.add_part(Part(111, 100))
    robo.add_part(Part(111, 100))
    robo.add_part(MovablePart(777, 300, "TypeB"))
    robo.add_part(MovablePart(655, 300, "TypeA"))
    robo.add_part(MovablePart(755, 300, "TypeA"))
    robo.add_part(MovablePart(977, 300, "TypeB"))
    robo.display()
    print()
    
    print("\nRobot test flight----")
    robo.fly()
    
    print("\nRobot dowork() test ----")
    robo.dowork()
    
    print("\nDuplicated part list----")
    partfreq = robo.find_duplicated_parts()
    for partno in partfreq.keys():
        print(partno,'=>', partfreq[partno], 'times')
    
    print("\nExpensive part list----")
    expensive_parts = robo.get_expensive_parts(200)
    for part in expensive_parts:
        part.display()
    
    print("\nMovable part list----")
    movable_parts = robo.get_movable_parts_bytype()
    for type, parts in movable_parts.items():
        print("type =", type)
        for part in parts:
            part.display()
    print()

    print("\nAsk movable to move----")
    movable_parts = robo.get_movable_parts()
    for part in movable_parts:
        part.move()
    
    print("\nTest remove_part() ----")
    robo.remove_part(333)
    for part in robo.parts:
        if part.partno == 333:
            print('Found 333')
            break


if __name__=="__main__":
    main()

