from abc import ABC, abstractmethod
import random

class State(ABC):
    def gotApplication(self): 
        return self.doTask()
        
    def checkApplication(self): 
        return self.doTask()
        
    def rentApartment(self): 
        return self.doTask()
        
    def dispenseKeys(self): 
        return self.doTask()
        
    @abstractmethod
    def doTask(self):
        pass        
        
class RentingMachineInterface(ABC):
    @abstractmethod
    def gotApplication(self): 
        pass
    
    @abstractmethod
    def checkApplication(self): 
        pass
        
    @abstractmethod
    def rentApartment(self): 
        pass
    
    @abstractmethod
    def setState(self, state): 
        pass
        
    @abstractmethod
    def getWaitingState(self): 
        pass
        
    @abstractmethod
    def getGotApplicationState(self): 
        pass
        
    @abstractmethod
    def getApartmentRentedState(self): 
        pass
        
    @abstractmethod
    def getFullyRentedState(self): 
        pass
    
    @abstractmethod
    def getCount(self): 
        pass
        
    @abstractmethod
    def setCount(self, n): 
        pass
    

class RentingMachine(RentingMachineInterface):
    def __init__(self, n):
        self.count = n;
        self.waitingState = WaitingState(self)
        self.gotApplicationState = GotApplicantState(self) 
        self.apartmentRentedState = ApartmentRentedState(self) 
        self.fullyRentedState =FullyRentedState(self)
        self.state = self.waitingState

    def gotApplication(self):
        print(self.state.gotApplication())
        
    def checkApplication(self):
        print(self.state.checkApplication())
        
    def rentApartment(self):
        print(self.state.rentApartment())
        print(self.state.dispenseKeys())
        
    def getWaitingState(self):
        return self.waitingState
        
    def getApartmentRentedState(self):
        return self.apartmentRentedState
        
    def getGotApplicationState(self):
        return self.gotApplicationState
        
    def getFullyRentedState(self):
        return self.fullyRentedState
        
    def getCount(self):
        return self.count;
        
    def setCount(self, n):
        self.count = n
        
    def setState(self, state):
        self.state = state
        
class WaitingState(State):
    def __init__(self, machine):
        self.machine = machine
        
    def gotApplication(self):
        self.machine.setState(self.machine.getGotApplicationState())
        return "Thanks for the application!"
        
    def doTask(self):
        return "You may not have applied or your application is pending."
        
        
class GotApplicantState(State):
    def __init__(self, machine):
        self.machine = machine
        
    def checkApplication(self):
        # simulate the chances for the application to be approved.
        approved = random.randint(0, 9) > 3
        
        if approved == True:
            self.machine.setState(self.machine.getApartmentRentedState())
            return "Congratulations, you were approved."
        else:
            self.machine.setState(self.machine.getWaitingState())
            return "Sorry, you were not approved."
        
    def doTask(self):
        return "You must have your application checked."
        
class ApartmentRentedState(State):
    def __init__(self, machine):
        self.machine = machine
        
    def doTask(self):
        return "Hang on, we're renting you an apartment."
        
    def rentApartment(self):
        self.machine.setCount(self.machine.getCount() - 1);
        return "Renting you an appartment"
        
    def dispenseKeys(self):
        if (self.machine.getCount() <= 0):
            self.machine.setState(self.machine.getFullyRentedState())
        else:
            self.machine.setState(self.machine.getWaitingState())
        return "Here are your keys!"
        
class FullyRentedState(State):
    def __init__(self, machine):
        self.machine = machine
        
    def doTask(self):
        return "Sorry, we're fully rented."
       
def showMenu():
	print("COMMAND MENU")
	print("apply - Submit Application")
	print("check - Check Application")
	print("rent - Rent Appartment")
	print("exit - Exit program")
	print() 
        
def main():
    machine = RentingMachine(9) 
    showMenu()
    
    while True:        
        command = input("Command: ")
        if command == "apply":
            machine.gotApplication()
        elif command == "check":
            machine.checkApplication()
        elif command == "rent":
            machine.rentApartment()
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")
            
    
if __name__ == "__main__":
    main()
    