from abc import ABC, abstractmethod

class TV:
    def play_channel(self):
        print("The TV is playing a program on a channel.")

    
class Washer:
    def settemp_wash(self):
        print("The Washer is setting a water temperature to wash clothes.")


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class TVCommand(Command):
    def __init__(self, tv: TV) -> None:
        self.__tv = tv

    def execute(self):
        self.__tv.play_channel()


class WasherCommand(Command):
    def __init__(self, washer: Washer) -> None:
        self.__washer = washer

    def execute(self):
        self.__washer.settemp_wash()


def main():
    tv = TV()
    washer = Washer()


    # Invoker
    invoker: list[Command] = []
    invoker.append(TVCommand(tv))
    invoker.append(WasherCommand(washer))
    invoker.append(TVCommand(tv))


    # do something else


    for com in invoker:
        com.execute()




if __name__=="__main__":
    main()