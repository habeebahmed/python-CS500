from time import sleep
from balloon_twister_manager import (BalloonTwisterManager, ControlFacade,
                                     HolidayManager, Scheduler)
from helper import DisplayHelper, SortHelper


class BalloonTwisterApp:
    def __init__(self) -> None:
        dis_helper = DisplayHelper()
        sort_helper = SortHelper()
        bt_mg = BalloonTwisterManager(dis_helper, sort_helper)
        h_mg = HolidayManager(dis_helper, sort_helper)
        scheduler = Scheduler(h_mg, bt_mg)
        self.__controller: ControlFacade = ControlFacade(
            bt_mg, h_mg, scheduler)
        self.__controller.load_data()
        self.__scheduler = self.__controller.scheduler
        self.__holiday_mgr = self.__controller.holiday_manager

    def display_menu(self):
        print("####### Balloon Twisters Management Application #######")
        print("####### Developed By Habeeb(19716) with ❤️ #######\n")

        print("""
        MENU:\n
                1. SCHEDULE a balloon twister for customer
                2. CANCEL the reservation
                3. STATUS of Holiday or Balloon Twister
                4. DROPOUT Balloon Twister
                5. SIGNUP Balloon Twister
                6. SAVE and QUIT
                """)

    def process_input(self, option: int):

        if option == 1:
            try:
                print("Balloon Twister booking process started......")
                customer_name = input("Please enter the customer name: ")
                not_found = True
                holiday = ""
                while not_found:
                    holiday = input(
                        "Please enter the holiday(if incorrect you would need to re-enter): ").lower()
                    not_found = self.__holiday_mgr.check_holiday(holiday)

                self.__scheduler.book_balloon_twister(customer_name, holiday)
                print("Balloon Twister booked!!!")
                sleep(2)
                return True
            except Exception as e:
                print("Something went wrong while scheduling, please try again \n", e)
        elif option == 2:
            try:
                print("Cancelling reservation......")
                customer_name = input("Please enter the customer name: ")
                not_found = True
                holiday = ""
                while not_found:
                    holiday: str = input(
                        "Please enter the holiday(if incorrect you would need to re-enter): ").lower()
                    not_found: bool = self.__holiday_mgr.check_holiday(holiday)
                self.__scheduler.cancel_reservation(customer_name, holiday)
                sleep(2)
                return True
            except Exception as e:
                print(
                    "Something went wrong while removing reservation, please try again \n", e)
        elif option == 3:
            try:
                print("Retrieve Status of \n1. Balloon Twister\n2. Holiday")
                selection = int(input("Please enter the appropriate option: "))
                if selection == 1:
                    # retrieve BT schedule
                    bt_name: str = input("Please enter Balloon twister name: ")
                    self.__scheduler.get_status_of_bt(bt_name)
                elif selection == 2:
                    # retrieve Holiday schedule
                    holiday: str = input("Please enter Holiday: ")
                    self.__scheduler.get_status_of_holiday(holiday)
                sleep(2)
                return True
            except Exception as e:
                print(
                    "Something went wrong while retrieving status, please try again \n", e)
        elif option == 4:
            print("DropOut Balloon Twister")
            bt_name: str = input("Please enter Balloon twister name: ")
            self.__scheduler.dropout_bt(bt_name)
            return True

        elif option == 5:
            print("Signup new Balloon Twister")
            bt_name: str = input("Please enter Balloon twister name: ")
            self.__scheduler.signup_bt(bt_name)
            return True

        elif option == 6:
            print("Saving Data......")
            self.__controller.save_data()
            print("Data saved successfully")
            print("Quitting Application")
            return False


def main():
    bt = BalloonTwisterApp()
    confirm = True
    while confirm:
        bt.display_menu()
        selection: int = int(
            input("\nPlease select the option from above menu: "))
        confirm = bt.process_input(selection)


if __name__ == "__main__":
    main()
