import enum
import random

class State(enum.Enum): 
    FULLY_RENTED = 1
    WAITING = 2 
    GOT_APPLICATION = 3
    APARTMENT_RENTED = 4
    
class RentalMethods:
    def __init__(self, n):
        self.numberApartments = n
        self.state = State.WAITING
        
    def getApplication(self):
        if self.state == State.FULLY_RENTED:
            print("Sorry, we’re fully rented.")
        elif self.state == State.WAITING:
            self.state = State.GOT_APPLICATION
            print("Thanks for the application.")
        elif self.state == State.GOT_APPLICATION:
            print("We already got your application.")
        elif self.state == APARTMENT_RENTED:
            print("Hang on, we’re renting you an apartment.")
            
    def checkApplication(self):
        if self.state == State.FULLY_RENTED:
            print("Sorry, we’re fully rented.")
        elif self.state == State.WAITING:
            print("You have to submit an application.")
        elif self.state == State.GOT_APPLICATION:
            # simulate the chances for the application to be approved.
            approved = random.randint(0, 9) > 3
            
            if approved == True:
                print("Congratulations, you were approved.")
                self.state = State.APARTMENT_RENTED
                self.rentApartment()
            else:
                print("Sorry, you were not approved.")
                state = State.WAITING;
        elif self.state == State.APARTMENT_RENTED:
            print("Hang on, we're renting you an apartment")
            
    def rentApartment(self):
        if self.state == State.FULLY_RENTED:
            print("Sorry, we’re fully rented.")
        elif self.state == State.WAITING:
            print("You have to submit an application.")
        elif self.state == State.GOT_APPLICATION:
            print("You must have your application checked.")
        elif self.state == State.APARTMENT_RENTED:
            print("Renting you an apartment ....")
            self.numberApartments -= 1
            self.despenseKeys()
            
    def despenseKeys(self):
        if self.state == State.FULLY_RENTED:
            print("Sorry, we’re fully rented.")
        elif self.state == State.WAITING:
            print("You have to submit an application.")
        elif self.state == State.GOT_APPLICATION:
            print("You must have your application checked.")
        elif self.state == State.APARTMENT_RENTED:
            print("Here are your keys!")

def main():
    rentalMethods = RentalMethods(9) 
    rentalMethods.getApplication() 
    rentalMethods.checkApplication()
    
if __name__ == "__main__":
    main()
    