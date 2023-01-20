# Write a method rectangleOfSymbols that displays a solid rectangle of symbols whose height and width are
# specified in integer parameter “height” and “width” respectively. And this method also receive a third parameter
# of type char called “fillCharacter”. For example, if height is 5, weight is 4, and the fillCharacter is *, the method
# should display
# ****
# ****
# ****
# ****
# ****
# Create a main method that reads the height, width and symbol of the user and then calls the
# rectangleOfSymbols method to display the rectangle of symbols.


def rectangleOfSymbols(height, weight, symbol):
    for i in range(height):
        for j in range(weight):
            print(symbol, end="")
        print()


def main():
    print('Print a rectangle of symbols')
    height = int(input("Enter the height: "))
    weight = int(input("Enter the weight: "))
    symbol = input("Enter the symbol: ")
    rectangleOfSymbols(height, weight, symbol)


if __name__ == "__main__":
    main()




