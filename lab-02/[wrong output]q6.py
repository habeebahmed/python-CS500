# Write a method triangleOfSymbols that displays a solid triangle of symbols whose height is specified in integer
# parameter “height”, the symbol is specified in string parameter “fillCharacter”. For example, if height is 4 and
# the fillCharacter is *, the method should display
#    *
#   ***
#  *****
# *******
# Create a main method that reads the height and symbol of the user and then calls the triangleOfSymbols
# method to display the triangle of symbols.


from symtable import Symbol


def triangleOfSymbols(height, symbol):
    k = height - 1
    # outer loop to handle number of rows

    for i in range(0, height):
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
        # decrementing k after each loop
        k = k - 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1): 
           # printing symbol

            print("{} ".format(symbol), end="")

        # ending line after each row

        print("\r")

def main():
    print("Display solid triangle with provided symbol")
    # read height and symbol entered by user
    height = int(input("Please enter the height of triangle: "))
    symbol = input("Please enter the symbol: ")
    triangleOfSymbols(height, symbol)

if __name__ == "__main__":
    main()
