from typing import List


class Schedule:
    def __init__(self, balloon_twister_name: str, holiday: str, customer_name: str) -> None:
        self.__balloon_twister_name: str = balloon_twister_name
        self.__holiday: str = holiday
        self.__customer_name: str = customer_name
    
    @property
    def balloon_twister_name(self):
        return self.__balloon_twister_name

    @property
    def holiday(self):
        return self.__holiday

    @property
    def customer_name(self):
        return self.__customer_name

    @customer_name.setter
    def customer_name(self, name: str):
        self.__customer_name = name
    
    @balloon_twister_name.setter
    def balloon_twister_name(self, name: str):
        self.__balloon_twister_name = name

class DisplayHelper:
    def print_schedule(self, schedules: List[Schedule], type: str):
        if type == 'bt' and schedules:
            print(f"Schedule for {schedules[0].balloon_twister_name}")
            print("Holiday\tCustomer Name")
            print("----------------------")
            for schedule in schedules:
                print(f"{schedule.holiday}  {schedule.customer_name}")
        elif type == 'hd' and schedules:
            print(f"Schedule for {schedules[0].holiday}")
            print("Customer Name\tBalloon Twister")
            print("------------------------------")
            for schedule in schedules:
                print(f"{schedule.customer_name}  {schedule.balloon_twister_name}")
        else:
            print("*****NO DATA******")

class SortHelper:
    def sort_by_type(self, schedules: List[Schedule], type: str) -> List[Schedule]:
        sorted_list = sorted(schedules, key=lambda x: getattr(x,type))
        return sorted_list