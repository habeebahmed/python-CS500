import os
from time import sleep
from typing import Dict, List, Optional, Union

from db import StandardDataExtractor
from helper import DisplayHelper, Schedule, SortHelper


class HolidayManager:
    def __init__(self, dis_helper: DisplayHelper, sort_helper: SortHelper) -> None:
        self.__holidays: Dict[str, List[Schedule]] = {}
        self.__dis_helper = dis_helper
        self.__sort_helper = sort_helper

    def load_holidays(self, schedules:  List[Schedule] = []):
        factory: StandardDataExtractor = StandardDataExtractor()
        reader2 = factory.read_data(os.path.join(
            os.path.dirname(__file__), "Holidays.dat"), "txt")
        holiday_data = []
        if reader2:
            holiday_data = reader2.get_data()

        for hd in holiday_data:
            self.__holidays[hd] = [x for x in schedules if x.holiday == hd]
            # self.__holidays[hd] = next((x for x in schedules if x.holiday == hd), [])
        
        # Sorting logic by customer
        for key, value in self.__holidays.items():
            self.__holidays[key] = self.__sort_helper.sort_by_type(value, "customer_name")

    def check_holiday(self, holiday: str):
        return not any(x == holiday for x in self.__holidays)

    def add_reservation(self, schedule: Schedule):
        self.__holidays[schedule.holiday].append(schedule)

    def remove_reservation(self, schedule: Schedule):
        self.__holidays[schedule.holiday] = list(filter(
            lambda x: x.customer_name != schedule.customer_name, self.__holidays[schedule.holiday]))

    def get_schedule_by_holiday(self, holiday: str):
        holiday_schedule: List[Schedule] = self.__holidays[holiday]
        self.__dis_helper.print_schedule(holiday_schedule, 'hd')

    def update_reservation_schedule(self, schedule: Schedule, old_bt_name: str):
        self.__holidays[schedule.holiday] = list(map(lambda x: schedule if x.balloon_twister_name ==
                                                     old_bt_name and x.customer_name == schedule.customer_name else x, self.__holidays[schedule.holiday]))


class BalloonTwisterManager:
    def __init__(self, dis_helper: DisplayHelper, sort_helper: SortHelper) -> None:
        # {"bt_name": [Schedule]}
        self.__balloon_twisters: Dict[str, List[Schedule]] = {}
        self.__dis_helper = dis_helper
        self.__sort_helper = sort_helper
        self.__factory: StandardDataExtractor = StandardDataExtractor()

    def load_balloon_twister(self, schedules: List[Schedule] = []) -> None:
        reader2 = self.__factory.read_data(os.path.join(
            os.path.dirname(__file__), "BalloonTwisters.dat"), "txt")
        bt_data = []
        if reader2:
            bt_data = reader2.get_data()

        for bt in bt_data:
            self.__balloon_twisters[bt] = [
                x for x in schedules if x.balloon_twister_name == bt]
            # self.__balloon_twisters[bt] = next((x for x in schedules if x.balloon_twister_name == bt), [])
        # Sorting logic by holiday
        for key, value in self.__balloon_twisters.items():
            self.__balloon_twisters[key] = self.__sort_helper.sort_by_type(value, "holiday")

    def get_available_balloon_twister(self):
        available_bt: list[str] = [
            key for key, value in self.__balloon_twisters.items() if not value]
        return available_bt[0] if len(available_bt) > 0 else None

    def add_bt_schedule(self, schedule: Schedule):
        self.__balloon_twisters[schedule.balloon_twister_name].append(schedule)

    def remove_schedule(self, schedule: Schedule):
        self.__balloon_twisters[schedule.balloon_twister_name] = list(filter(
            lambda x: x.customer_name != schedule.customer_name and x.holiday != schedule.holiday, self.__balloon_twisters[schedule.holiday]))

    def get_bt_schedule_by_name(self, bt_name: str):
        bt_schedule: List[Schedule] = self.__balloon_twisters[bt_name]
        self.__dis_helper.print_schedule(bt_schedule, 'bt')

    def add_bt(self, bt_name: str):
        self.__balloon_twisters[bt_name] = []

    def save_data(self):
        bt_data: list[str] = list(self.__balloon_twisters.keys())
        writer = self.__factory.write_data(os.path.join(
            os.path.dirname(__file__), "BalloonTwisters.dat"), "txt")
        if writer:
            writer.save_data(bt_data)

    def get_schedule(self, bt_name: str):
        return self.__balloon_twisters[bt_name]

    def remove_bt(self, bt_name: str):
        self.__balloon_twisters.pop(bt_name)


class Scheduler:
    def __init__(self, h_mgr: HolidayManager, bt_mgr: BalloonTwisterManager) -> None:
        self.__schedule_list: List[Schedule] = []
        # List containing { customer_name: "Habeeb", holiday: "Labor Day" }
        self.__waiting_list: List[Dict[str, str]] = []
        self.__bt_manager = bt_mgr
        self.__h_manager = h_mgr
        self.__factory: StandardDataExtractor = StandardDataExtractor()

    @property
    def schedule_list(self):
        return self.__schedule_list

    def load_schedules(self):
        reader = self.__factory.read_data(os.path.join(
            os.path.dirname(__file__), "schedule.csv"), "csv")
        data_scheduler_List = []
        if reader:
            data_scheduler_List = reader.get_data(Schedule)
            self.__schedule_list = data_scheduler_List

        return data_scheduler_List

    def save_data(self):
        writer = self.__factory.write_data(os.path.join(
            os.path.dirname(__file__), "schedule.csv"), "csv")
        if writer:
            writer.save_data(self.schedule_list)

    def book_balloon_twister(self, customer_name: str, holiday: str):
        available_bt: Optional[str] = self.__bt_manager.get_available_balloon_twister(
        )
        # If balloon_twister available
        if available_bt:
            schedule = Schedule(available_bt, holiday, customer_name)
            self.__h_manager.add_reservation(schedule)
            self.__bt_manager.add_bt_schedule(schedule)
            self.__schedule_list.append(schedule)
        else:
            self.__waiting_list.append(
                {customer_name: customer_name, holiday: holiday})

    def find_schedule(self, customer_name: str, holiday: str) -> Union[Schedule, Dict]:
        return next((x for x in self.__schedule_list if x.customer_name == customer_name and x.holiday == holiday), {})

    def cancel_reservation(self, customer_name: str, holiday: str):
        remove_schedule: Schedule = self.find_schedule(customer_name, holiday)
        if remove_schedule:
            # Remove reservation
            self.__h_manager.remove_reservation(remove_schedule)

            # remove Balloon twister schedule
            self.__bt_manager.remove_schedule(remove_schedule)

            # Remove from schedule list
            self.__schedule_list.remove(remove_schedule)



    def get_status_of_bt(self, bt_name: str):
        self.__bt_manager.get_bt_schedule_by_name(bt_name)

    def get_status_of_holiday(self, holiday: str):
        self.__h_manager.get_schedule_by_holiday(holiday)

    def signup_bt(self, bt_name: str):
        self.__bt_manager.add_bt(bt_name)
        print(f"Balloon Twister {bt_name} added to the list!!")
        sleep(2)

    def dropout_bt(self, bt_name: str):
        bt_schedule: List[Schedule] = self.__bt_manager.get_schedule(bt_name)
        print(f"Found {len(bt_schedule)} schedule for {bt_name}")
        for schedule in bt_schedule:
            bt_replacement: Optional[str] = self.__bt_manager.get_available_balloon_twister(
            )
            if bt_replacement:
                print(f"Replacing {bt_name} with {bt_replacement} for holiday - {schedule.holiday}")
                schedule.balloon_twister_name = bt_replacement
                self.__bt_manager.add_bt_schedule(schedule)
                self.__h_manager.update_reservation_schedule(
                    schedule, bt_name)
                index: int = next((index for (index, d) in enumerate(
                    self.__schedule_list) if d.customer_name == schedule.customer_name and d.holiday == schedule.holiday), -1)
                self.__schedule_list[index].balloon_twister_name = bt_replacement
            else:
                print(f"Adding customer - {schedule.customer_name} with schedule for holiday - {schedule.holiday} to top of the waiting list")
                self.__waiting_list.insert(
                    0, {"customer_name": schedule.customer_name, "holiday": schedule.holiday})
        self.__bt_manager.remove_bt(bt_name)
        print(f"Balloon Twister {bt_name} removed from the list")


class ControlFacade:
    def __init__(self, bt_manager: BalloonTwisterManager, holiday_manager: HolidayManager, scheduler: Scheduler) -> None:
        self.__bt_manager = bt_manager
        self.__holiday_manager = holiday_manager
        self.__scheduler = scheduler

    @property
    def bt_manager(self):
        return self.__bt_manager

    @property
    def holiday_manager(self):
        return self.__holiday_manager

    @property
    def scheduler(self):
        return self.__scheduler

    def load_data(self):
        print("Loading data........")
        load_schedules = self.__scheduler.load_schedules()
        self.__bt_manager.load_balloon_twister(load_schedules)
        self.__holiday_manager.load_holidays(load_schedules)
        sleep(2)
        print("Data loaded successfully!!!!")

    def save_data(self):
        self.__scheduler.save_data()
        self.__bt_manager.save_data()
