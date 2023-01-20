from abc import ABC, abstractmethod
from typing import Dict, List


class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class AbstractCompany(ABC):
    def __init__(self) -> None:
        self._max_num_employees: int = 10

    @abstractmethod
    def get_employee_name_list(self) -> List[str]:
        pass


class Employee(Displayable):
    def __init__(self, empid: int, name: str, salary: float, title: str) -> None:
        self.__empid: int = empid
        self.__name = name
        self.__salary = salary
        # [TODO] use enum class?
        self.__title: str = title

    @property
    def empid(self) -> int:
        return self.__empid

    @property
    def title(self) -> str:
        return self.__title

    @property
    def name(self) -> str:
        return self.__name

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, sal: float) -> None:
        self.__salary: float = sal

    def display(self) -> None:
        print(
            f"=====Employee Details===== \nEmpId = {self.__empid}\nName = {self.__name}\nSalary = {self.__salary}\nTitle={self.__title}")


class Company(Displayable, AbstractCompany):
    def __init__(self, comp_name: str) -> None:
        AbstractCompany.__init__(self)
        self.__comp_name: str = comp_name
        self.__employees: list[Employee] = []
        self.place: int = 0

    @property
    def employees(self) -> List[Employee]:
        return self.__employees

    def add_employee(self, employee: Employee) -> None:
        if len(self.__employees) > self._max_num_employees:
            print("Compnay has reached maximum number of employee")
            return
        self.__employees.append(employee)

    def remove_employee(self, empid: int) -> None:
        index: int = next((index for (index, d) in enumerate(
            self.__employees) if d.empid == empid), -1)
        if index != -1:
            self.__employees.pop(index)

    def update_employee_salary(self, empid: int, salary: float):
        for emp in self.__employees:
            if (emp.empid == empid):
                emp.salary = salary
                break

    def get_employee_name_list(self) -> List[str]:
        return list(map(lambda x: x.name, self.__employees))

    # def __itr__(self):
    #     self.__emp_init: int = -1
    #     return self

    # def __next__(self) -> Employee | None:
    #     if (self.__emp_init >= len(self.__employees)-1):
    #         return None
    #     self.__emp_init += 1
    #     emp: Employee = self.__employees[self.__emp_init]
    #     return emp

    def __itr__(self):
        """
        Return an iterator that allows you to iterate over the set of
        employees, one employee at a time
        """
        self.place = 0
        return self

    def __next__(self) -> Employee:
        if self.place >= len(self.__employees):
            raise StopIteration
        self.place = self.place + 1
        return self.__employees[self.place-1]

    def display(self) -> None:
        print(f"Company name: {self.__comp_name}")



class StockBusiness(Displayable):
    def __init__(self, research_tool: str, comission_rate: float) -> None:
        self.__research_tool: str = research_tool
        self.__comission_rate: float = comission_rate

    def trade(self, stock_name: str) -> None:
        print(f"trading {stock_name}")

    def display(self) -> None:
        print(f"Research Tool: {self.__research_tool}\nComission Rate: {self.__comission_rate}")


class TradingCompany(Company, StockBusiness):
    def __init__(self, comp_name: str, product_type: str, number_of_offices: int, research_tool: str, comission_rate: float) -> None:
        Company.__init__(self, comp_name)
        StockBusiness.__init__(self, research_tool, comission_rate)
        self.__product_type = product_type
        self.__number_of_offices = number_of_offices

    def get_employees_high_salary(self, limit: float) -> List[Employee]:
        return list(filter(lambda x: x.salary > limit, self.employees))

    def get_employees_by_title(self) -> Dict[str, List[str]]:
        dict_employees: dict[str, list[str]] = {}
        for emp in self.employees:
            if emp.title not in dict_employees:
                dict_employees[emp.title] = [emp.name]
            else:
                dict_employees[emp.title].append(emp.name)
        
        return dict_employees

    def display(self) -> None:
        print(f"Product Type: {self.__product_type}\nNumber of offices: {self.__number_of_offices}")
        print()
        Company.display(self)
        print()
        StockBusiness.display(self)
        print()
        for emp in self.employees:
            emp.display()
            print()


def main() -> None:
    trade_comp: TradingCompany = TradingCompany("Tesla", "Car", 10, "Motors", 7.5)
    trade_comp.trade("BMW")
    print()
    emp1: Employee = Employee(111, 'Habeeb', 172199137193.09, 'Officer')
    emp2: Employee = Employee(222, 'Ahmed', 120.9, 'Supervisor')
    emp3: Employee = Employee(333, 'New Bee', 19137193.29, 'Officer')
    emp4: Employee = Employee(444, 'Worker', 5999.10, 'Manager')
    emp5: Employee = Employee(555, 'Outlier', 999999.10, 'Manager')
    trade_comp.add_employee(emp1)
    trade_comp.add_employee(emp2)
    trade_comp.add_employee(emp3)
    trade_comp.add_employee(emp4)
    trade_comp.add_employee(emp5)
    trade_comp.display()

    trade_comp.remove_employee(555)

    print("\nEmployees after removing id 555")

    trade_comp.display()

    trade_comp.update_employee_salary(222, 45909)
    print("\nEmployees after updating salary of id 222")
    
    trade_comp.display()

    emps: List[Employee] = trade_comp.get_employees_high_salary(45000)
    print("\nEmployees with high salary than 45000\n")
    for emp in emps:
        emp.display()

    print()
    print("List Employees by title\n")
    emp_dict_by_title: Dict[str, List[str]] = trade_comp.get_employees_by_title()
    for emp_title in emp_dict_by_title.keys():
        print(f"{emp_title}: {', '.join(emp_dict_by_title[emp_title])}")    

if __name__ == "__main__":
    main()

