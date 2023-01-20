from __future__ import annotations
from typing import List

class Person:
    def __init__(self, name: str) -> None:
        self.__name: str = name

    @property
    def name(self) -> str:
        return self.__name

    def display(self):
        print("name =", self.__name)

    def dowork(self):
        print("Person ", self.__name, "is doing nothing.")


class Programmer(Person):
    def __init__(self, name: str, skills: str, salary: float) -> None:
        super().__init__(name)
        self.__skills: str = skills
        self.__salary: float = salary

    def display(self) -> None:
        super().display()
        print("skills =", self.__skills)
        print("salary =", self.__salary)

    def dowork(self) -> None:
        print("programmer ", self.name, "is writing a program")

    def get_annual_income(self) -> float:
        return self.__salary * 12


class Manager(Programmer):
    def __init__(self, name: str, skills: str, salary: float, bonus: float) -> None:
        super().__init__(name, skills, salary)
        self.__bonus: float = bonus

    def display(self) -> None:
        super().display()
        print("bonus =", self.__bonus)

    def dowork(self) -> None:
        print("Manager ", self.name, "is supervising a team of programmers")

    def get_annual_income(self) -> float:
        return super().get_annual_income() + self.__bonus


class Project:
    def __init__(self, projname: str, budget: float = 0.0, active: bool = False) -> None:
        self.__projname: str = projname
        self.__budget: float = budget
        self.__active: bool = active

    @property
    def budget(self) -> float:
        return self.__budget

    @property
    def active(self) -> bool:
        return self.__active

    def display(self) -> None:
        print("projname =", self.__projname)
        print("budget =", self.__budget)
        print("active =", self.__active)


class Group:
    def __init__(self, groupname: str) -> None:
        self.__groupname = groupname
        self.__members: list[Programmer] = []

    def add_member(self, member: Programmer) -> None:
        self.__members.append(member)

    def remove_member(self, name: str) -> None:
        index: int = next((index for (index, d) in enumerate(self.__members) if d.name == name), -1)
        if index != -1:
            self.__members.pop(index)

    def ask_anyone_dowork(self) -> None:
        for member in self.__members:
            member.dowork()

    def ask_manager_dowork(self) -> None:
        for member in self.__members:
            if isinstance(member, Manager):
                member.dowork()

    def get_allmembers_morethan(self, income: float) -> list[Programmer]:
        member_greater_income_list: List[Programmer] = []
        for mem in self.__members:
            if mem.get_annual_income() > income:
                member_greater_income_list.append(mem)
        return member_greater_income_list

    def display(self) -> None:
        print("The group has these members")
        for member in self.__members:
            member.display()
            print()


class ITGroup(Group):
    def __init__(self, groupname: str) -> None:
        super().__init__(groupname)
        self.__projects: list[Project] = []

    def add_project(self, project: Project) -> None:
        self.__projects.append(project)

    def find_largest_project(self) -> Project | None:
        max_proj: Project | None = None
        for prj in self.__projects:
            if max_proj == None:
                max_proj = prj
            else:
                max_proj = prj
        return max_proj

    def get_active_projects(self) -> List[Project]:
        return list(filter(lambda x: x.active, self.__projects))

    def display(self) -> None:
        super().display()
        print("The group has these projects:")
        for prj in self.__projects:
            prj.display()
            print()


def main() -> None:
    p1: Programmer = Programmer("Lily", "C++, Java", 10000)
    p2: Programmer = Programmer("Judy", "Python, Java", 18000)
    m: Manager = Manager("Peter", "Management", 20000, 20000)
    proj1: Project = Project("MAX-5", 200000, True)
    proj2: Project = Project("FOX-4", 100000, False)
    proj3: Project = Project("FOX-XP", 500000, True)
    itgrp: ITGroup = ITGroup("ATX Group")
    itgrp.add_member(p1)
    itgrp.add_member(p2)
    itgrp.add_member(m)
    itgrp.add_project(proj1)
    itgrp.add_project(proj2)
    itgrp.add_project(proj3)
    itgrp.display()
    p3: Programmer = Programmer("Jone", "Python, Java", 1118000)
    itgrp.add_member(p3)
    print()
    itgrp.ask_anyone_dowork()
    print()
    itgrp.ask_manager_dowork()
    print("\nGet the largest project...")
    maxProj: Project | None = itgrp.find_largest_project()
    if (maxProj):
        maxProj.display()

    print("\nGet the acive projects...")
    projects: list[Project] = itgrp.get_active_projects()
    for proj in projects:
        proj.display()
        print()
    print()
    itgrp.remove_member(p3.name)
    itgrp.display()

    print("\nGet the members with high income...")
    members: list[Programmer] = itgrp.get_allmembers_morethan(200000)
    for member in members:
        member.display()
        print()
    print()


if __name__ == "__main__":
    main()
