from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

class Subject(ABC):
    @abstractmethod
    def registerObserver(self, o):
        pass
    @abstractmethod
    def removeObserver(self, o):
        pass
    @abstractmethod
    def notifyObserver(self):
        pass    
class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass

class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class House(Displayable):
    def __init__(self, address: str, squareFeet: int, numRooms: int, price: float) -> None:
        self.__address: str = address
        self.__squareFeet: int = squareFeet
        self.__numRooms: int = numRooms
        self.__price: float = price

    # add some public properties here if necessary
    @property
    def address(self) -> str:
        return self.__address
    
    def change_price(self, new_price: float):
        self.__price = new_price

    def display(self) -> None:
        print(f"Address = {self.__address}, Square Feet = {self.__squareFeet}, Num of Rooms = {self.__numRooms}, Price = {self.__price}")

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, House):
            if self.__address == __o.__address:
                return  True
            
        return False


class Contact(Displayable):
    def __init__(self, firstName: str, lastName: str, phoneNumber: str, email: str) -> None:
        self.__lastName: str = lastName
        self.__firstName: str = firstName
        self.__email: str = email
        self.__phoneNumber: str = phoneNumber

    # add some public properties here if necessary
    @property
    def lastName(self) -> str:
        return self.__lastName

    @property
    def firstName(self) -> str:
        return self.__firstName

    @property
    def email(self) -> str:
        return self.__email

    @property
    def phoneNumber(self) -> str:
        return self.__phoneNumber

    def display(self) -> None:
        pass

class Owner(Observer, Contact):
    def __init__(self, lastName: str, firstName: str, phoneNumber: str, email: str) -> None:
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__houses: list[House] = []

    def addHouse(self, house: House):
        self.__houses.append(house)

    def display(self) -> None:
        print(f"Last Name = {self.lastName}, First Name = {self.firstName}, Phone Number = {self.phoneNumber}, Email = {self.email}")
        for house in self.__houses:
            house.display()
    def update(self, source):
        print(self.firstName, "got the notice")
        # source.display()
        print()

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Owner):
            if (self.email == __o.email):
                return True
        return False


class Buyer(Observer, Contact):
    def __init__(self, lastName: str, firstName: str, phoneNumber: str, email: str) -> None:
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__watchList: list[House] = []

    @property
    def watchList(self) -> List[House]:
        return self.__watchList

    #  Save the house in his watch list 
    def saveForLater(self, house: House) -> None:
        if house not in self.__watchList:
            self.__watchList.append(house)

    # Remove the house from his watch list
    def removeFromSaveForLater(self, house: House) -> None:
        if house in self.__watchList:
            self.__watchList.remove(house)

    def display(self) -> None:
        print(f"Last Name = {self.lastName}, First Name = {self.firstName}, Phone Number = {self.phoneNumber}, Email = {self.email}")
        print("Watching the following houses:")
        for house in self.__watchList:
            house.display()

    def update(self, source):
        print(self.firstName, "got the notice")
        # source.display()
        print()

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Buyer):
            if (self.email == __o.email):
                return True
        return False


class Company(Subject, Displayable):
    def __init__(self, companyName: str):
        self.__companyName: str = companyName
        self.__owners: list[Owner] = []
        self.__buyers: list[Buyer] = []
        self.__agents: list[Agent] = []
        self.__houses: list[House] = []
        self.__observers = []

    def registerObserver(self, o):
        self.__observers.append(o)

    def removeObserver(self, o):
        i = self.__observers.index(o)
        if i >= 0:
            self.__observers.pop(i)

    def addOwner(self, owner: Owner):
        if owner not in self.__owners:
            self.__owners.append(owner)

    def addBuyer(self, buyer: Buyer):
        if buyer not in self.__buyers:
            self.__buyers.append(buyer)

    def addAgent(self, agent: Agent):
        if agent not in self.__agents:
            self.__agents.append(agent)

    def addHouseToListing(self, house: House):
        if house not in self.__houses:
            self.__houses.append(house)

    def getHouseByAddress(self, address: str) -> House | None:
        for house in self.__houses:
            if house.address == address:
                return house
        return None
    
    def updateHouseByAddress(self, address: str, newPrice: float):
        house_new_price = None
        for house in self.__houses:
            if house.address == address:
                house_new_price = house
                break
        if house_new_price:
            house_new_price.change_price(newPrice)
            self.notifyObserver(self)

    def removeHouseFromListing(self, house: House):
        if house in self.__houses:
            self.__houses.remove(house)
            self.notifyObserver(self)


    # Help to remove that house from all buyers' watch list.
    def removeHouseFromSaveForLater(self, house: House):
        for buyer in self.__buyers:
            buyer.removeFromSaveForLater(house)
            self.notifyObserver(self)

    def getBuyersByHouse(self, house: House) -> List[Buyer]:
        buyers_house: list[Buyer] = []
        for buyer in self.__buyers:
            if house in buyer.watchList:
                buyers_house.append(buyer)
        return buyers_house

    def notifyObserver(self, data):
        for o in self.__observers:
            o.update(data)
            print()

    def display(self) -> None:
        print(f"Company Name = {self.__companyName}")
        print("=========================== The list of agents: ==============================")
        for agent in self.__agents:
            agent.display()
        print("=========================== The house listing: ===============================")
        for house in self.__houses:
            house.display()
        print("=========================== The list of owners: ==============================")
        for owner in self.__owners:
            owner.display()
        print("=========================== The list of buyers: ==============================")
        for buyer in self.__buyers:
            buyer.display()


class Agent(Observer, Contact):
    def __init__(self, lastName: str, firstName: str, phoneNumber: str, email: str, position: str, company: Company):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__position: str = position
        self.__company: Company = company

    def addHouseToListingForOwner(self, owner: Owner, house: House) -> None:
        self.__company.addOwner(owner)
        self.__company.addHouseToListing(house)

    def helpBuyerToSaveForLater(self, buyer: Buyer, house: House):
        self.__company.addBuyer(buyer)
        buyer.saveForLater(house)

    # Observer notified
    def editHousePrice(self, address: str, newPrice: float):
        self.__company.updateHouseByAddress(address, newPrice)

    # Observer notified
    def soldHouse(self, house: House):
        self.__company.removeHouseFromListing(house)
        self.__company.removeHouseFromSaveForLater(house)

    # print all potential buyers who are interested in buying that house
    def printPotentalBuyers(self, house: House):
        potentialBuyers: List[Buyer] = self.__company.getBuyersByHouse(house)
        for buyer in potentialBuyers:
            buyer.display()

    def display(self):
        print(f"Last Name = {self.lastName}, First Name = {self.firstName}, Phone Number = {self.phoneNumber}, Email = {self.email} Position = {self.__position}")

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Agent):
            if (self.email == __o.email):
                return True
        return False

    def update(self, source):
        print(self.firstName, "got the notice")
        # source.display()
        print()


def main() -> None:
    owner1: Owner = Owner('Peter', 'Li', '510-111-2222', 'peter@yahoo.com')
    owner2: Owner = Owner('Carl', 'Buck', '408-111-2222', 'carl@yahoo.com')

    house1: House = House('1111 Mission Blvd', 1000, 2, 1000000)
    house2: House = House('2222 Mission Blvd', 2000, 3, 1500000)
    house3: House = House('3333 Mission Blvd', 3000, 4, 2000000)

    owner1.addHouse(house1)
    owner2.addHouse(house2)
    owner2.addHouse(house3)

    buyer1: Buyer = Buyer('Tom', 'Buke', '408-555-2222', 'tom@yahoo.com')
    buyer2: Buyer = Buyer('Lily', 'Go', '510-222-3333', 'lily@yahoo.com')

    company: Company = Company('Good Future Real Estate')
    agent1: Agent = Agent('Dave', 'Henderson', '408-777-3333',
                   'dave@yahoo.com', 'Senior Agent', company)
    company.addAgent(agent1)

    # Add Oberver code
    company.registerObserver(owner1)
    company.registerObserver(owner2)
    company.registerObserver(buyer1)
    company.registerObserver(buyer2)
    company.registerObserver(agent1)

    agent1.addHouseToListingForOwner(owner1, house1)
    agent1.addHouseToListingForOwner(owner2, house2)
    agent1.addHouseToListingForOwner(owner2, house3)

    agent1.helpBuyerToSaveForLater(buyer1, house1)
    agent1.helpBuyerToSaveForLater(buyer1, house2)
    agent1.helpBuyerToSaveForLater(buyer1, house3)

    agent1.helpBuyerToSaveForLater(buyer2, house2)
    agent1.helpBuyerToSaveForLater(buyer2, house3)

    print('\nAfter one house price updated ..........................')
    agent1.editHousePrice('2222 Mission Blvd', 1200000)

    company.display()

    print('\nAfter one house was sold ..........................')
    agent1.soldHouse(house3)
    company.display()

    print('\nDisplaying potential buyers for house 1 ..........................')
    agent1.printPotentalBuyers(house1)



if __name__ == "__main__":
    main()