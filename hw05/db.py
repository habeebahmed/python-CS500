from __future__ import annotations

import csv
import os
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, List, Optional, Union

from helper import Schedule

if TYPE_CHECKING:
    from balloon_twister_manager import Schedule

# from customer import Customer

class BaseExtractor(ABC):
    def __init__(self, file_name: str) -> None:
        self.__file_name = file_name

    @property
    def file_name(self) -> str:
        return self.__file_name

    @abstractmethod
    def get_data(self, wrapperClass: Optional[Schedule] = None) -> Union[List[List[str]], List[Schedule], List[None], List[str]]:
        pass

    @abstractmethod
    def save_data(self, data_list: Union[List[None], List[Schedule], List[str]]) -> None:
        pass

class CSVRead(BaseExtractor):
    def get_data(self, wrapperClass: Optional[Schedule] = None) -> Union[List[List[str]], List[Schedule], List[None]]:
        rows: Union[List[List[str]], List[Schedule], List[None]] = []
        with open(self.file_name, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                data: Optional[Union[Schedule, List[str]]] = wrapperClass(
                    row[0], # balloon_twister_name
                    row[1], # holiday
                    row[2], # customer_name
                ) if wrapperClass else row
                rows.append(data)
            return rows
    
    def save_data(self, data_list: Union[List[None], List[Schedule], List[str]]) -> None:
        raise NotImplementedError

class CSVWrite(BaseExtractor):
    def save_data(self, data_list: Union[List[None], List[Schedule], List[Any]]) -> None:
        with open(self.file_name, "w", newline="") as file:
            writer = csv.writer(file)
            rows: list[list[str | int | float]] = []
            for row in data_list:
                if isinstance(row, Schedule):
                    rows.append([row.balloon_twister_name, row.holiday, row.customer_name])
                elif row and len(row) == 3:
                    rows.append([row[0], row[1], row[2]])
            
            writer.writerows(rows)

    def get_data(self, wrapperClass: Optional[Schedule] = None) -> List[str]:
        raise NotImplementedError

class TXTRead(BaseExtractor):
    def get_data(self, wrapperClass: Optional[Schedule] = None) -> List[str]:
        with open(self.file_name) as file:
            lines: list[str] = [line.rstrip() for line in file]
        return lines

    def save_data(self, data_list: Union[List[None], List[Schedule], List[str]]) -> None:
        raise NotImplementedError

class TXTWrite(BaseExtractor):
    def get_data(self, wrapperClass: Optional[Schedule] = None) -> List[str]:
        raise NotImplementedError

    def save_data(self, data_list: Union[List[None], List[Schedule], List[str]]) -> None:
        with open(self.file_name, 'w') as f:
            for line in data_list:
                if line and isinstance(line, str):
                    f.write(line)
                    f.write('\n')

class AbstractFactory:
    def read_data(self, file_name: str, type: str) -> Optional[Union[CSVRead, TXTRead]]:
        pass

    
    def write_data(self, file_name: str, type: str) ->Optional[Union[CSVWrite, TXTWrite]]:
        pass

class StandardDataExtractor(AbstractFactory):
    def read_data(self, file_name: str, type: str) -> Optional[Union[CSVRead, TXTRead]]:
        rd = None
        if type == "csv":
            rd = CSVRead(file_name)
        elif type == "txt":
            rd = TXTRead(file_name)

        return rd

    def write_data(self, file_name: str, type: str) -> Optional[Union[CSVWrite, TXTWrite]]:
        wt = None
        if type == "csv":
            wt = CSVWrite(file_name)
        elif type == "txt":
            wt = TXTWrite(file_name)
        
        return wt


def main() -> None:
    factory: StandardDataExtractor = StandardDataExtractor()
    reader: CSVRead | TXTRead | None = factory.read_data(os.path.join(os.path.dirname(__file__), "Holidays.dat"), "txt")
    reader2: CSVRead | TXTRead | None = factory.read_data(os.path.join(os.path.dirname(__file__), "BalloonTwisters.dat"), "txt")
    reader3 = factory.read_data(os.path.join(os.path.dirname(__file__), "schedule.csv"), "csv")
    writer3 = factory.write_data("schedule.csv", "csv")
    data_scheduler: List[Schedule] = []
    if reader:
        reader.get_data()
    if reader2:
        reader2.get_data()
    if reader3:
        data_scheduler = reader3.get_data(Schedule)
    
    if data_scheduler and len(data_scheduler) > 0 and writer3:
        data_scheduler[0].customer_name = "Hacking"  
        writer3.save_data(data_scheduler)


if __name__=="__main__":
    main()