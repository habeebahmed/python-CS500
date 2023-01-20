import random

from state_machine import (Event, InvalidStateTransition, State,
                           acts_as_state_machine, after, before)


@acts_as_state_machine
class RentingProcess:
    gotApplication = State(initial=True)
    apartmentRented = State()
    waiting = State()
    accept = State()
    exit = State()

    # define transitions
    check_info = Event(from_states=gotApplication, to_state=waiting)
    disapprove = Event(from_states=waiting, to_state=gotApplication)
    approve = Event(from_states=waiting, to_state=apartmentRented)
    accepted = Event(from_states=apartmentRented, to_state=gotApplication)
    back = Event(from_states=waiting, to_state=gotApplication)

    def __init__(self, name: str):
        self.name: str = name

    @before('check_info')
    def check_info_info(self):
        print(f'{self.name} said Thanks for the application!')

    @before('approve')
    def approve_info(self):
        print(f'{self.name} is checking the application')

    @after('approve')
    def approve_info(self):
        print(f'{self.name} said Congratulations, you were approved.')

    @before('disapprove')
    def disapprove_info(self):
        print(f'{self.name} entered into waiting state')

    @after('disapprove')
    def disapprove_info(self):
        print(f'Sorry, you were not approved.')

    @after('accepted')
    def accepted_info(self):
        print(f'{self.name} entered into waiting state')

    @before('accepted')
    def accepted_info(self):
        print(f'Here are your keys!')

    @after('back')
    def back_info(self):
        print(f'Bye!')


class RentingMachine:
    def __init__(self, name: str) -> None:
        self.__process = RentingProcess(name)

    def show_menu(self):
        print("COMMAND MENU")
        print("apply - Submit Application")
        print("check - Check Application")
        print("rent - Rent Apartment")
        print("exit - Exit program")

    def begin_application(self):
        try:
            self.__process.check_info()
        except InvalidStateTransition as err:
            print(
                f"Error: {self.__process.name} cannot get application in {self.__process.current_state} state")


    def verify_application(self):
        approved = random.randint(0,9) > 3
        try:
            if approved is True:
                self.__process.approve()
            else:
                self.__process.disapprove()
                
        except InvalidStateTransition as err:
            print(
                f"Error: {self.__process.name} check application in {self.__process.current_state} state")

    def rent_house(self):
        try:
            self.__process.accepted()
        except InvalidStateTransition as err:
            print(
                f"Error: {self.__process.name} cannot enter check info in {self.__process.current_state} state")        


    def back_to_checkout(self):
        try:
            self.__process.back()
        except InvalidStateTransition as err:
            print(
                f"Error: {self.__process.name} cannot return to application in {self.__process.current_state} state")


def main() -> None:
    system = RentingMachine("Alex")

    while True:
        system.show_menu()
        command = input("Command: ")
        if command == "apply":
            system.begin_application()
        elif command == "check":
            system.verify_application()
        elif command == "rent":
            system.rent_house()
        elif command == "exit":
            print("Bye")
            break


if __name__ == "__main__":
    main()

