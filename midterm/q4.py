class Item:

    def __init__(self, name):

        self.__name = name
    
    @property
    def name(self):
        return self.__name


class MyList:

    def __init__(self):

        self.__items = []

    def add_item(self, item):

        self.__items.append(item)

    def remove_item(self, item: Item):
        name = item.name
        index: int = next((index for (index, d) in enumerate(
            self.__items) if d.name == name), -1)
        if index != -1:
            self.__items.pop(index)



def main():

    mylist = MyList()

    for i in range(3):

        name = input("Enter an item name to add: ")

        mylist.add_item(Item(name))

    name = input("Enter an item name to remove: ")

    mylist.remove_item(Item(name))


main()
