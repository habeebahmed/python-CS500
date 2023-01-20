class Hand:
    def __init__(self, num_fingers: int):
        self.__num_fingers = num_fingers

    def __str__(self) -> str:
        return "Hand has " + str(self.__num_fingers) + " fingers"


class Person:
    # def __init__(self, name, age, lhand, rhand):
    #     self.__name = name
    #     self.__age = age
    #     self.__lhand = lhand
    #     self.__rhand = rhand
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
        self.__lhand: Hand = Hand(5) # composition
        self.__rhand: Hand = Hand(5) # composition

    def get_names(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return "Person's name = " + self.__name \
            +  ", age = " + str(self.__age) \
            + ", lhand = " + str(self.__lhand) \
            + ", rhand = " + str(self.__rhand)

def main() -> None:
    lhand = Hand(5)
    print(lhand)
    rhand = Hand(5)

    person = Person("Dave", 25)
    # person = Person("Dave", 25, lhand, rhand)
    print(person)

if __name__ == "__main__":
    main()