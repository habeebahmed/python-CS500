from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str) -> None:
        self.__name: str = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def dowork(self):
        pass


class Student(Person):
    def __init__(self, name: str, gpa: float) -> None:
        super().__init__(name)
        self.__gpa: float = gpa

    def dowork(self):
        print(f"Student {self.name} is doing homework.")


class Teacher(Person):
    def __init__(self, name: str, salary: float) -> None:
        super().__init__(name)
        self.__salary: float = salary

    def dowork(self):
        print(f"Teacher {self.name} is teaching a class.")


class SkillDecorator(Person):       # abstract class
    def __init__(self, person: Person) -> None:
        self._person: Person = person   # protected


class StudySkill(SkillDecorator):
    def __init__(self, person: Person) -> None:
        super().__init__(person)

    def dowork(self) -> None:
        self._person.dowork()
        print("Student is also studying a lots of tutorials")


class TeachSkill(SkillDecorator):
    def __init__(self, person: Person) -> None:
        super().__init__(person)

    def dowork(self) -> None:
        self._person.dowork()
        print("Also writing a research paper.")


class DesignSkill(SkillDecorator):
    def __init__(self, person: Person) -> None:
        super().__init__(person)

    def dowork(self) -> None:
        self._person.dowork()
        print("Also designing a new device.")


def main() -> None:
    s1: Student = Student("Peter", 3.5)
    s1.dowork()
    print("========================")
    s1 = StudySkill(s1)
    s1.dowork()
    print("========================")
    s1 = TeachSkill(s1)
    s1.dowork()
    print("========================")
    s1 = DesignSkill(s1)
    s1.dowork()
    print("========================")
    s2: DesignSkill = DesignSkill(StudySkill(Student("Lily", 3.0)))
    s2.dowork()


main()
