from __future__ import annotations
import itertools
import csv
from typing import List

def read_files(students: list[Student], courses:list[Course]):
    student_files_to_read: list[str] = ["students.csv"]
    course_files_to_read: list[str] = ["CS500.csv", "CS480.csv", "CS360.csv"]

    for std in student_files_to_read:
        with open(std, newline="") as file:
            reader = csv.reader(file)
            for (index, row) in enumerate(reader):
                students[index].id = row[0]
                students[index].name = row[1]
                students[index].course = row[2:]

    for (index, course) in enumerate(course_files_to_read):
        with open(course, newline="") as file:
            reader = csv.reader(file)
            course_number = course.split(".")[0]
            courses[index].course_number = course_number
            for row in reader:
                courses[index].student_scores[row[0]] = [int(x) for x in row[1:]]

            



def write_summary(students: list[Student], courses:list[Course]):
        with open("summary.csv", "w+", newline="") as file:
            writer = csv.writer(file)
            rows = []
            #    1234,Ken,CS480,10.0,CS500,10.0

            #     2222,David,CS360,9.25,CS500,7.5

            #     3333,Judy,CS480,7.25
            rows = []
            for student in students:
                print(student.id)
                course_by_no = filter(lambda x: x.course_number in student.course ,courses)
                course_with_grade = [[cour.course_number, cour.get_grades(student.id)]for cour in course_by_no]
                course_with_grade =list(itertools.chain.from_iterable(course_with_grade))
                print(course_with_grade)
                row = [student.id, student.name]
                row.extend(course_with_grade)
                # print(row)
                rows.append(row)
            
            writer.writerows(rows)


class Student:
    def __init__(self) -> None:
        self.__id = ""
        self.__name = ""
        self.__course: List[str] = []

    @property
    def id(self) -> str:
        return self.__id
    @property
    def name(self) -> str:
        return self.__name
    @property
    def course(self) -> List[str]:
        return self.__course

    @id.setter
    def id(self, id: str):
        self.__id = id

    @name.setter
    def name(self, name: str):
        self.__name = name

    @course.setter
    def course(self, course: List[str]):
        self.__course = course

    def __str__(self) -> str:
        return f"{self.id} {self.name}"

    def __repr__(self) -> str:
        return str(self)

class Course:
    def __init__(self) -> None:
        self.__course_number = ""
        self.__student_scores: dict[str, List[int]] = {}
    
    @property
    def course_number(self) -> str:
        return self.__course_number
    
    @property
    def student_scores(self) -> dict[str, List[int]]:
        return self.__student_scores

    @course_number.setter
    def course_number(self, course_number: str):
        self.__course_number = course_number 

    @student_scores.setter
    def student_scores(self, student_scores:dict[str, List[int]]):
        self.__student_scores = student_scores 

    def get_grades(self, student_id: str):
        student_scores = self.student_scores[student_id].copy()
        del student_scores[student_scores.index(max(student_scores))]
        del student_scores[student_scores.index(min(student_scores))]
        return sum(student_scores)/len(student_scores)

    def __str__(self) -> str:
        return f"{self.course_number} {self.student_scores}"

    def __repr__(self) -> str:
        return str(self)  


def main():
    student1 = Student()
    student2 = Student()
    student3 = Student()
    course1 = Course()
    course2 = Course()
    course3 = Course()
    student_list = [student1, student2, student3]
    course_list = [course1, course2, course3]
    read_files(student_list, course_list)
    print(student_list)
    print(course_list)
    write_summary(student_list, course_list)

if __name__=="__main__":
    main()