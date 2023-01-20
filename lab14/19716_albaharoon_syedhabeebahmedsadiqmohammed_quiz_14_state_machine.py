import random

from state_machine import (Event, InvalidStateTransition, State,
                           acts_as_state_machine, after, before)


@acts_as_state_machine
class CheckoutProcess:
    checkout = State(initial=True)
    payment = State()
    pending = State()
    confirmed = State()
    canceled = State()

    # define transitions
    payment_info = Event(from_states=checkout, to_state=payment)
    submit_order = Event(from_states=payment, to_state=pending)
    disapprove = Event(from_states=pending, to_state=checkout)
    approve = Event(from_states=pending, to_state=confirmed)
    cancel = Event(from_states=confirmed, to_state=canceled)
    back = Event(from_states=(confirmed, canceled), to_state=checkout)

    def __init__(self, name: str):
        self.name: str = name

    @before('payment_info')
    def payment_info_info(self):
        print(f'{self.name} said please enter your credit card information!')

    @before('submit_order')
    def submit_order_info(self):
        print(
            f'{self.name} received the order request and we are verifying your order.')

    @after('approve')
    def approve_info(self):
        print(f'{self.name} said Congratulations, your order is now complete.')

    @after('disapprove')
    def disapprove_info(self):
        print(f'{self.name} said sorry your order was not approved, please remove some items in your shopping cart.')

    @after('cancel')
    def cancel_info(self):
        print(f'{self.name} said sorry to hear you cancel your order, but I am glad to help.')

    @after('back')
    def back_info(self):
        print(f'{self.name} said good to see you coming back.')


class OrderSystem:
    def __init__(self, name: str) -> None:
        self.__process = CheckoutProcess(name)

    def show_menu(self):
        print("COMMAND MENU")
        print("begin - Begin Checkout")
        print("submit - Submit your order")
        print("cancel - Cancel my order")
        print("return - Back to Checkout")
        print("exit - Exit program")

    def begin_checkout(self):
        try:
            self.__process.payment_info()
        except InvalidStateTransition as err:
            print(
                f"Error: {self.__process.name} cannot enter payment info in {self.__process.current_state} state")

    def submit_order(self):
        try:
            self.__process.submit_order()
            self.verify_order()
        except InvalidStateTransition as err:
            print(
                f"Error: {self.__process.name} cannot submit order in {self.__process.current_state} state")

    def verify_order(self):
        approved = random.randint(0,9) > 3
        try:
            if approved is True:
                self.__process.approve()
            else:
                self.__process.disapprove()
                
        except InvalidStateTransition as err:
            print(
                f"Error: {self.__process.name} cannot submit order in {self.__process.current_state} state")

    def cancel_order(self):
        try:
            self.__process.cancel()
        except InvalidStateTransition as err:
            print(
                f"Error: {self.__process.name} cannot cancel order in {self.__process.current_state} state")

    def back_to_checkout(self):
        try:
            self.__process.back()
        except InvalidStateTransition as err:
            print(
                f"Error: {self.__process.name} cannot return to checkout in {self.__process.current_state} state")


def main() -> None:
    system = OrderSystem("Alex")

    while True:
        system.show_menu()
        command = input("Command: ")
        if command == "begin":
            system.begin_checkout()
        elif command == "submit":
            system.submit_order()
        elif command == "cancel":
            system.cancel_order()
        elif command == "return":
            system.back_to_checkout()
        elif command == "exit":
            print("Bye")
            break


if __name__ == "__main__":
    main()
