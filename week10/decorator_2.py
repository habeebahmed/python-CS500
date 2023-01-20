from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, number: int, color: str) -> None:
        self.__vehicle_number: int = number
        self.__color: str = color

    @property
    def vehicle_number(self) -> int:
        return self.__vehicle_number

    @property
    def color(self) -> str:
        return self.__color

    @abstractmethod
    def vehicle_status(self) -> None:
        pass

    @abstractmethod
    def vehicle_info(self) -> None:
        pass


class Car(Vehicle):
    def __init__(self, number: int, color: str, type: str) -> None:
        super().__init__(number, color)
        self.__type: str = type

    def vehicle_status(self) -> None:
        print(f"Car with registration number -> {self.vehicle_number} is in good condition")

    def vehicle_info(self) -> None:
        print(f"Car Info: \nVehicle number: {self.vehicle_number}\nColor: {self.color}\nType: {self.__type}")

class Truck(Vehicle):
    def __init__(self, number: int, color: str, truck_class: str) -> None:
        super().__init__(number, color)
        self.__truck_class: str = truck_class

    def vehicle_status(self) -> None:
        print(f"Truck with reg. number {self.vehicle_number} is loading goods")

    def vehicle_info(self) -> None:
        print(f"Truck Info:\nVehicle number: {self.vehicle_number}\nColor: {self.color}\nClass: {self.__truck_class}")

class ModifierDecorator(Vehicle):
    def __init__(self, vehicle: Vehicle) -> None:
        self._vehicle: Vehicle = vehicle
    
class CarTyreModifier(ModifierDecorator):
    def __init__(self, vehicle: Vehicle, size: str) -> None:
        super().__init__(vehicle)
        self.__tyre_size: str = size

    def vehicle_info(self) -> None:
        self._vehicle.vehicle_info()
        print("Upgraded typres with size ", self.__tyre_size)

    def vehicle_status(self) -> None:
        self._vehicle.vehicle_status()
        print("Car tyres being upgraded")

class CarExhaustModifier(ModifierDecorator):
    def __init__(self, vehicle: Vehicle) -> None:
        super().__init__(vehicle)

    def vehicle_info(self) -> None:
        self._vehicle.vehicle_info()
        print("Updated car exhaust")

    def vehicle_status(self) -> None:
        self._vehicle.vehicle_status()
        print("Car exhaust is being upgraded")


class TruckSizeModifier(ModifierDecorator):
    def __init__(self, vehicle: Vehicle) -> None:
        super().__init__(vehicle)

    def vehicle_info(self) -> None:
        self._vehicle.vehicle_info()
        print("Attached carrier to truck")

    def vehicle_status(self) -> None:
        self._vehicle.vehicle_status()
        print("Truck is being attached carrier")

def main():
    v1: Car = Car(151, "black", "Sedan")
    v2: Truck = Truck(255, "White", "Half-Ton Truck")

    v1.vehicle_status()
    print()
    v1.vehicle_info()
    print("\n\n==================")
    v2.vehicle_status()
    print()
    v2.vehicle_info()

    print("\n\n==================")
    v1 = CarTyreModifier(v1, "Large")
    v1.vehicle_status()
    print()
    v1.vehicle_info()


    print("\n\n==================")
    v1 = CarExhaustModifier(v1)
    v1.vehicle_status()
    print()
    v1.vehicle_info()

    print("\n\n==================")
    v2 = TruckSizeModifier(v2)
    v2.vehicle_status()
    print()
    v2.vehicle_info()


main()