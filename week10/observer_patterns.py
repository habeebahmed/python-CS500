from abc import ABC, abstractmethod
import enum
class Subject(ABC):
    @abstractmethod
    def registerObserver(self, o):
        pass
    @abstractmethod
    def removeObserver(self, o):
        pass
    @abstractmethod
    def notifyObserver(self):
        pass    
class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass
class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass
class CourseData(Subject, Displayable):
    def __init__(self):
        self.__observers = []
        self.__averageAttendance = 0.0
        self.__averageScore = 0.0
    def registerObserver(self, o):
        self.__observers.append(o)
    def removeObserver(self, o):
        i = self.__observers.index(o)
        if i >= 0:
            self.__observers.pop(i)
    @property
    def averageAttendance(self):
        return self.__averageAttendance
    @property
    def averageScore(self):
        return self.__averageScore
    @averageAttendance.setter
    def averageAttendance(self, value):
        if self.__averageAttendance != value:
            self.__averageAttendance = value
            self.notifyObserver(self)
    @averageScore.setter
    def averageScore(self, value):
        if self.__averageScore != value:
            self.__averageScore = value
            self.notifyObserver()
    def notifyObserver(self, data):
        for o in self.__observers:
            o.update(data)
            print()
    def display(self):
        print('Average Attendance = ', self.__averageAttendance)
        print('Average Score = ', self.__averageScore)
class Professor(Observer, Displayable):
    def __init__(self, name):
        self.__name = name
        
    def display(self):
        print("name =", self.__name)
        
    def update(self, source):
        print(self.__name, "got the notice")
        source.display()
        print()
def main():
    courseData = CourseData()
    prof1 = Professor('Henry')
    courseData.registerObserver(prof1)
    prof2 = Professor('Jack')
    courseData.registerObserver(prof2)
    courseData.averageAttendance = 75.5
main()