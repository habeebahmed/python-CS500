# ● Implement the following classes according to the following class diagrams.
# ● After you implement all the classes, write a main method to create objects of the classes you defined and
# print out their contents.
# ● Each class should have appropriate setters and getters using property annotation for accessing private
# attributes
# ● The House class should allow other classes to
# ○ add and remove a TV object the televisions list.
# ○ change the garage object’s size
# ● The House class should also have the following public methods:
# ○ def get_biggest_room(self) -> Room
# ■ Based on the size of the room, find the largest one.
# ○ def get_oled_televisions(self) -> list[Television]
# ■ Get a list of televisions with an OLED display
# ○ def is_siimilar_house(self, other) -> bool
# ■ If two houses have the same square footage and number of rooms, they are considered similar
from __future__ import annotations
from typing import List


class Garage:
    def __init__(self, type: str, size: int, door_type: str) -> None:
        self.__type: str = type
        self.__size: int = size
        self.__door_type: str = door_type

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str) -> None:
        self.__type = type

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int) -> None:
        self.__size = size

    @property
    def door_type(self) -> str:
        return self.__door_type

    @door_type.setter
    def door_type(self, door_type: str) -> None:
        self.__door_type = door_type

    def __str__(self) -> str:
        return "Garage: Type = {}, Size(sqft) = {} and Door type = {}".format(
            self.type, self.size, self.door_type)


class Television:
    def __init__(self, telId: int, screen_type: str, screen_size: int, resolution: str, price: float) -> None:
        self.__screen_type: str = screen_type
        self.__screen_size: int = screen_size
        self.__resolution: str = resolution
        self.__price: float = price
        self.__telId: int = telId

    @property
    def telId(self) -> int:
        return self.__telId

    @property
    def screen_type(self) -> str:
        return self.__screen_type

    @screen_type.setter
    def screen_type(self, screen_type: str) -> None:
        self.__screen_type = screen_type

    @property
    def screen_size(self) -> int:
        return self.__screen_size

    @screen_size.setter
    def screen_size(self, screen_size: int) -> None:
        self.__screen_size = screen_size

    @property
    def resolution(self) -> str:
        return self.__resolution

    @resolution.setter
    def resolution(self, resolution: str) -> None:
        self.__resolution = resolution

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        self.__price = price

    def __str__(self) -> str:
        return "Screen Type = {}, Screen Size = {}, Resolution = {} and Price = {}".format(
            self.screen_type, self.screen_size, self.resolution, self.price)


class Room:
    def __init__(self, roomNo: int, type: str, size: int) -> None:
        self.__type: str = type
        self.__size: int = size
        self.__roomNo: int = roomNo

    @property
    def roomNo(self) -> int:
        return self.__roomNo

    @roomNo.setter
    def roomNo(self, roomNo: int) -> None:
        self.__roomNo = roomNo

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str) -> None:
        self.__type = type

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int) -> None:
        self.__size = size

    def __str__(self) -> str:
        return "Type = {} and Size(sqft) = {}".format(self.type, self.size)


class House:
    def __init__(self, address: str, square_feet: int, garage: Garage) -> None:
        self.__address: str = address
        self.__square_feet: int = square_feet
        # self.__garage: Garage = garage
        self.__garage: Garage = Garage(
            garage.type, garage.size, garage.door_type)  # composition
        self.__rooms: list[Room] = []
        self.__televisions: list[Television] = []

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str) -> None:
        self.__address = address

    @property
    def square_feet(self) -> int:
        return self.__square_feet

    @square_feet.setter
    def square_feet(self, square_feet: int) -> None:
        self.__square_feet = square_feet

    @property
    def garage(self) -> Garage:
        return self.__garage

    def add_room(self, roomNo: int, type: str, size: int) -> None:  # composition
        if len(self.__rooms) == 4:
            print("Maximum number of rooms reached")
            return
        self.__rooms.append(Room(roomNo, type, size))

    def remove_room(self, roomNo: int) -> None:
        index: int = next((index for (index, d) in enumerate(
            self.__rooms) if d.roomNo == roomNo), -1)
        if index != -1:
            self.__rooms.pop(index)

    def add_television(self, tel: Television) -> None:
        self.__televisions.append(tel)

    def remove_television(self, telId: int) -> None:
        index: int = next((index for (index, d) in enumerate(
            self.__televisions) if d.telId == telId), -1)
        if index != -1:
            self.__televisions.pop(index)

    def change_garage_size(self, size: int) -> None:
        self.garage.size = size

    def get_biggest_room(self) -> Room | None:
        bigRoom: Room | None = None
        for room in self.__rooms:
            if bigRoom == None:
                bigRoom = room
            if room.size > bigRoom.size:
                bigRoom = room
        return bigRoom

    # https://stackoverflow.com/a/52623912 return type if list
    def get_oled_televisions(self) -> List[Television]:
        return list(filter(lambda x: x.screen_type == 'OLED', self.__televisions))

    # reference class House within class House by putting the type annotation in quotes. This is called forward reference.
    # https://github.com/python/mypy/issues/3661
    # https://www.youtube.com/watch?v=AJsrxBkV3kc
    def is_similar_house(self, other: House) -> bool:
        return bool(self.__square_feet == other.__square_feet and len(self.__rooms) == len(other.__rooms))

    def __str__(self) -> str:
        houselist: str = ""
        houselist += "House Details: \nAddress:{}, square ft: {}\n\nGarage details:\n{}".format(
            self.address, self.square_feet, self.garage)
        houselist += "\n\nRoom details:\n"

        for room in self.__rooms:
            houselist += str(room) + "\n"

        if self.__televisions:
            houselist += "\nTelevisions:\n"
            for tel in self.__televisions:
                houselist += str(tel) + "\n"
        return houselist


def main() -> None:

    print("House 1\n")
    g: Garage = Garage("single", 100, "auto")
    h: House = House("irvine st", 122, g)
    # h.add_garage_info("single", 100, "auto")
    h.add_room(101, "store room", 200)
    h.add_room(102, "Bed room", 500)
    h.add_room(201, "Living room", 600)
    print(h)
    h.remove_room(102)
    print(h)
    h.add_television(Television(221, "OLED", 65, '1080px', 500))
    h.add_television(Television(225, "OLED", 85, '1080px', 800))
    h.add_television(Television(222, "LCD", 65, '720px', 1500))
    h.add_television(Television(223, "LED", 65, '1080px', 2500))
    h.remove_television(222)
    print(h)
    h.change_garage_size(500)
    print("Biggest room: ", h.get_biggest_room())
    oled_tvs: List[Television] = h.get_oled_televisions()
    if oled_tvs:
        print("\nTelevision having OLED displays")
        for tv in oled_tvs:
            print(tv)

    print("\n\nHouse 2\n")
    g2: Garage = Garage("double", 122, "auto")
    h2: House = House("stevenson st", 500, g2)
    h2.add_room(201, "store room", 400)
    h2.add_room(202, "Bed room", 400)
    h2.add_room(301, "Living room", 100)
    print(h2)
    print("\n")
    print("Are the houses similar ", h.is_similar_house(h2))


if __name__ == "__main__":
    main()
