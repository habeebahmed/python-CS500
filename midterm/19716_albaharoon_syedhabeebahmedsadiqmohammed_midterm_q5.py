from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, List, Optional, Union


class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class BuildingType(Enum):
    HEAVY_INDUSTRIAL: int = 0
    WAREHOUSE: int = 1
    COLD_STORAGE: int = 2
    LIGHT_INSUDTRIAL: int = 3
    DATA_HOUSING: int = 4


class Employee(Displayable):
    def __init__(self, emp_name: str, salary: float) -> None:
        self.__employee_name: str = emp_name
        self.__salary: float = salary

    @property
    def salary(self) -> float:
        return self.__salary

    @property
    def employee_name(self) -> str:
        return self.__employee_name

    def __str__(self) -> str:
        return f"Employee name = {self.__employee_name} , Salary =  {self.__salary}"

    def __repr__(self) -> str:
        return str(self)

    def display(self) -> None:
        print(self)


class Company(Displayable):
    def __init__(self, company_name: str) -> None:
        self.__company_name: str = company_name
        self.__employees: List[Employee] = []

    @property
    def employees(self):
        return self.__employees

    def add_employee(self, employee: Employee) -> None:
        self.__employees.append(employee)

    '''
        The method get_top_five_employees() delivers a list of the top five employees in terms of their salaries.
    '''

    def get_top_five_employees(self) -> List[Employee]:
        sorted_emp_by_sal: list[Employee] = sorted(
            self.__employees, key=lambda x: x.salary, reverse=True)
        return sorted_emp_by_sal[0:5]

    def get_employee(self, index: int) -> Employee:
        try:
            emp: Employee = self.__employees[index]
            return emp
        except IndexError:
            print("Index entered is out of range")
            raise (IndexError)

    def __str__(self) -> str:
        return f"Company Name: {self.__company_name}"

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
        self.place: int = self.place + 1
        return self.__employees[self.place-1]

    def display(self) -> None:
        print(self)


class Building(Displayable):
    def __init__(self, building_name: str, area: float, stories: int, type: BuildingType) -> None:
        self.__building_name: str = building_name
        self.__area: float = area
        self.__stories: int = stories
        self.__types: BuildingType = type
        self.__employees: List[Employee] = []

    @property
    def area(self):
        return self.__area

    @property
    def type(self):
        return self.__types

    def add_employee(self, employee: Employee) -> None:
        self.__employees.append(employee)

    def __str__(self) -> str:
        return f"Building Name = {self.__building_name}, Area = {self.__area}, Stories = {self.__stories}, Types = {self.__types}"

    def display(self) -> None:
        print(self)
        if self.__employees:
            print("Employees in building:")

        for emp in self.__employees:
            emp.display()
        print()

# Can only have 5 buildings


class ConstructionCompany(Company):
    def __init__(self, category: str, company_name: str) -> None:
        self.__category: str = category
        self.__buildings: List[Building] = []
        Company.__init__(self, company_name)

    def add_building(self, building: Building):
        if len(self.__buildings) > 5:
            print("Cannot add more than 5 buildings")
            return

        self.__buildings.append(building)

    def find_largest_building(self) -> Optional[Building]:
        largest_building: Optional[Building] = None
        for building in self.__buildings:
            if largest_building == None:
                largest_building = building
            elif largest_building.area < building.area:
                largest_building = building

        return largest_building

    def assign_employees_to_building(self, employee: Employee, b: Building):
        b.add_employee(employee)

    def get_buildings_by_types(self) -> Dict[str, List[Building]]:
        dict_buildings: dict[str, list[Building]] = {}
        for build in self.__buildings:
            if str(build.type) not in dict_buildings:
                dict_buildings[str(build.type)] = [build]
            else:
                dict_buildings[str(build.type)].append(build)

        return dict_buildings

    def __str__(self) -> str:
        return f"Category = {self.__category}"

    def display(self) -> None:
        print(self)
        for building in self.__buildings:
            building.display()


def main() -> None:
    e1: Employee = Employee("James", 133111.44)
    e2: Employee = Employee("Harries", 123111.14)
    e3: Employee = Employee("Warner", 134111.42)
    e4: Employee = Employee("Plato", 121311.09)
    e4: Employee = Employee("Warker", 121311.09)
    e4: Employee = Employee("talker", 12311.09)
    e4: Employee = Employee("user", 12111.09)

    b1: Building = Building('Free build', 1420.5, 5, BuildingType.COLD_STORAGE)
    b2: Building = Building('New Build', 1400.5, 5, BuildingType.WAREHOUSE)
    b3: Building = Building('Old Build', 1512.5, 5,
                            BuildingType.HEAVY_INDUSTRIAL)

    const_comp: ConstructionCompany = ConstructionCompany('Industry', 'Marvel Company')

    const_comp.add_employee(e1)
    const_comp.add_employee(e2)
    const_comp.add_employee(e3)
    const_comp.add_employee(e4)

    const_comp.add_building(b1)
    const_comp.add_building(b2)
    const_comp.add_building(b3)
    const_comp.assign_employees_to_building(e1, b2)

    const_comp.display()


    top_five_emp = const_comp.get_top_five_employees()
    print("Top Five employees")
    for emp in top_five_emp:
        print(emp)

    print()
    types: Dict[str, List[Building]] = const_comp.get_buildings_by_types()
    print("Building by types")
    for type in types:
        print(type)
        print()


    largest_building: Building | None = const_comp.find_largest_building()
    if largest_building:
        print(f"Largest building is {largest_building}")


if __name__ == "__main__":
    main()
