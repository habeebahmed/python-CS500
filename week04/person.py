class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property 
    def name(self):
        return self.__name
        
    @property 
    def age(self):
        return self.__age
        
    def display(self):
        print("name =", self.__name)
        print("age =", self.__age)
        
class Student(Person):
    def __init__(self, name, age, gpa):
        Person.__init__(self, name, age)
        self.__gpa = gpa
    
    @property 
    def gpa(self):
        return self.__gpa
        
    def display(self):
        Person.display(self)
        print("gpa =", self.__gpa)
        
    def study(self):
        print(self.name, "has been studying so hard")
        
class GraduateStudent(Student):
    def __init__(self, name, age, gpa, stipend):
        Student.__init__(self, name, age, age)
        self.__stipend = stipend
    
    @property 
    def stipend(self):
        return self.__stipend
        
    def display(self):
        Student.display(self)
        print("stipend =", self.__stipend)
        
    def gradeTest(self):
        print(self.name, "is grading students' tests.")
        
def main():
    p = Person("Peter", 20)
    s = Student("Nancy", 22, 3.5)
    g = GraduateStudent("Lily", 25, 3.8, 900.99)

    team = []
    team.append(p)
    team.append(s)
    team.append(g)
    
    for person in team:
        person.display()
        if isinstance(person, Student):
            person.study()
        if isinstance(person, GraduateStudent):
            person.gradeTest()   
        print()
        
        
    print("p is a person => ", isinstance(p, Person))
    print("s is a person => ", isinstance(s, Person))
    print("g is a person => ", isinstance(g, Person))
    print("g is a student => ", isinstance(g, Student))
    print("s is a graduate student => ", isinstance(s, GraduateStudent))
    
    
        
if __name__ == "__main__":
    main()