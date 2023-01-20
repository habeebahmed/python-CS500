class Student:
    def __init__(self, student_name: str, graduate: bool, program: str) -> None:
        self.__graduate: bool = graduate
        self.__student_name: str = student_name
        self.__program: str = program

    @property
    def graduate(self) -> bool:
        return self.__graduate

    @graduate.setter
    def graduate(self, val: bool) -> None:
        self.__graduate = val

    @property
    def student_name(self) -> str:
        return self.__student_name

    @student_name.setter
    def student_name(self, val: str) -> None:
        self.__student_name = val

    @property
    def program(self) -> str:
        return self.__program

    @program.setter
    def program(self, val: str) -> None:
        self.__program = val

    def __str__(self) -> str:
        is_graduated = "graduated" if self.graduate else "not graduacted"
        return f"{self.student_name} studying {self.program} and {is_graduated}"
        
    def __repr__(self) -> str:
        return str(self)


class School:
    def __init__(
        self,
        school_name: str = '',
        programs: list[str] = []
    ) -> None:
        self.__school_name: str = school_name
        self.__students: list[Student] = []
        self.__programs: list[str] = []
        for program in programs:
            self.__programs.append(program)

    def _str_(self) -> str:
        output = f"School Name = {self.__school_name}"
        output += "\nHas programs: \n"
        output += ", ".join(self.__programs)
        output += "\nHas students: \n"
        output += ", ".join([student.student_name for student in self.__students])
        return output
    
    def __repr__(self) -> str:
        return str(self)

    @property
    def school_name(self):
        return self.__school_name

    @school_name.setter
    def school_name(self, val):
        self.__school_name = val

    def add_student(self, student: Student) -> None:
        self.__students.append(student)
    
    def has_program(self, program: str) -> bool:
        return program in self.__programs

    def __iter__() -> None:
        pass

    def __next__() -> Student:
        pass


class College:
    def __init__(
        self,
        college_name: str,
    ) -> None:
        self.__college_name: str = college_name
        self.__schools: list[School] = []
        self.__students: list[Student] = []

    def _str_(self) -> str:
        output: str = f"College Name = {self.__college_name}"
        output += "\nHas Schools: \n"
        output += ", ".join([school.school_name for school in self.__schools])
        output += "\nHas students: \n"
        output += ", ".join([student.student_name for student in self.__students])
        return output


    def add_school(self, school_name: str, programs: list[str]) -> None:
        self.__schools.append(School(school_name, programs))

    def add_student(self, student: Student) -> None:
        self.__students.append(student)
        for school in self.__schools:
            if school.has_program(student.program):
                school.add_student(student)

    def get_students_by_program(self, program: str) -> list[Student]:
        output: list[Student] = []
        for student in self.__students:
            if student.program == program:
                output.append(student)

        return output


def main() -> None:
    s1: Student = Student('H1', True, 'MSCS')
    s2: Student = Student('H2', True, 'MBA')
    s3: Student = Student('H3', True, 'BA')
    s4: Student = Student('H4', True, 'BSC')

    college: College = College('SFBU')
    college.add_school("Business", ["BA", "MBA"])
    college.add_school("Engineering", ["MSCS", "BSC"])
    college.add_student(s1)
    college.add_student(s2)
    college.add_student(s3)
    college.add_student(s4)
    print(college)


if __name__ == "__main__":
    main()
