class Product:
    def __init__(self, name: str, price: float) -> None:
        self.__name: str = name
        self.__price: float = price
    def display(self) -> None:
        print(f"name = {self.__name}, pice = {self.__price}")


class Phone(Product):
    def __init__(self, name: str, price: float, network: str) -> None:
        Product.__init__(self, name, price)
        self.__network: str = network

    def display(self) -> None:
        super().display()
        print(f"network = {self.__network}")

class Computer(Product):
    def __init__(self, name: str, price: float, speed: float) -> None:
        Product.__init__(self, name, price)
        self.__speed: float = speed

    def display(self) -> None:
        super().display()
        print(f"speed = {self.__speed}")



class SmartPhone(Phone, Computer):
    def __init__(self, name: str, price: float, network: str, speed: float, camera: str) -> None:
    #  use this for multiple inheritance
        Phone.__init__(self, name, price, network)
        Computer.__init__(self, name, price, speed)
        self.__camera: str = camera
    
    def display(self) -> None:
        super().display()
        print(f"camera = {self.__camera}")

def main() -> None:
    sp: SmartPhone = SmartPhone("xphone", 1000, "5G", 3.5, "8K")
    print(vars(sp))
    sp.display()

if __name__ == "__main__":
    main()
