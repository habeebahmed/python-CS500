class Hand:

    def __init__(self, fingers):

        self.__fingers = fingers

        

class Person:

    def __init__(self, name, fingers):        

        self.__name = name

        self.__hands = [Hand(fingers), Hand(fingers)]

    

    @property

    def name(self):

        return self.__name

        

    @property

    def lh(self):

        return self.__hands[0]

    

    @property

    def rh(self):

        return self.__hands[1]

        

    @property

    def hands(self):

        return self.__hands