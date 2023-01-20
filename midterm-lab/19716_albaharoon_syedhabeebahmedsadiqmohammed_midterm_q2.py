from random import randrange


class Dice():
    def __init__(self) -> None:
        self.__dice: list[int] = []
        for i in range(4):
            self.__dice.append(randrange(2, 7, 2))

    @property
    def die1(self) -> int:
        return self.__dice[0]

    @property
    def die2(self) -> int:
        return self.__dice[1]

    @property
    def die3(self) -> int:
        return self.__dice[2]

    @property
    def die4(self) -> int:
        return self.__dice[3]

    def toss(self) -> int:
        sum = 0
        for (index, val) in enumerate(self.__dice):
            self.__dice[index] = randrange(7)
            sum += self.__dice[index]
        return sum

    def reset(self) -> None:
        for i in range(4):
            self.__dice[i] = randrange(2, 7, 2)


def main() -> None:
    d = Dice()
    no_times_dice_tossed: list[int] = []
    itr: int = 0
    confirm = "y"
    print("Initial Die values")
    print("Die1:", d.die1)
    print("Die2:", d.die2)
    print("Die3:", d.die3)
    print("Die4:", d.die4)
    while (confirm != "n"):
        sum: int = d.toss()
        itr += 1
        if (sum == 24):
            no_times_dice_tossed.append(itr)
            confirm: str = input("Continue? (y/n):")
            itr: int = 0
    print("Simulation results:\n")
    for (idx, val) in enumerate(no_times_dice_tossed):
        print("Simulation {}:   tossed {} times".format(idx+1, val))
    
    print("Resetting the dice values")
    d.reset()
    print("Die1:", d.die1)
    print("Die2:", d.die2)
    print("Die3:", d.die3)
    print("Die4:", d.die4)

if __name__ == "__main__":
    main()
