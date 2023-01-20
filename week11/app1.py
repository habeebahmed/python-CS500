from computers_factory import ComputerFactory, ComputerType


def show_types():
    print("Computer Types")
    for tp in ComputerType:
        print(f"{tp.value}. {tp.name}")

def main():
    show_types()
    computer_type = int(input("Please select a computer type number: "))
    cpu = input("Please enter a CPU: ")


    c = ComputerFactory().create_computer(ComputerType(computer_type), cpu)
    c.compute()


main()