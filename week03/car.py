class Engine:
    def __init__(self, horsepower):
        self.__horsepower = horsepower

    def __str__(self):
        return "Engine horsepower = " + str(self.__horsepower)


class Tire:
    def __init__(self, size):
        self.__size = size
    
    def __str__(self):
        return "Tire size = " + str(self.__size)

    
class Car:
    def __init__(self, model, year, horsepower):
        self.__model = model
        self.__year = year
        self.__engine: Engine = Engine(horsepower)
        self.__tires = []

    def add_tire(self, tire):
        self.__tires.append(tire)
    
    def __str__(self):
        tirestr = ", tire list: "
        for tire in self.__tires:
            tirestr += str(tire) + ", "

        return "Car model = " + self.__model \
                + ", year = " + str(self.__year) \
                + ", engine = " + str(self.__engine) + tirestr

def main():
    car1 = Car("X7", 2022, 280)
    car1.add_tire(Tire(20))
    car1.add_tire(Tire(21))
    car1.add_tire(Tire(22))
    car1.add_tire(Tire(23))

    print(car1)

if __name__ == "__main__":
    main()