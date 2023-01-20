# Write a Python program to implement a simple calculator.
# 1. Get two numbers and the operation desire
# 2. Check the operation
    # a. If the operation is addition, the result is the first + the second
    # b. If the operation is subtraction, the result is the first - the second
    # c. If the operation is multiplication, the result is the first * the second
    # d. If the operation is division, check the second number
        # i. If the second number is zero, construct an error message
        # ii. If the second number is not zero, the result is the first / the second
# 3. Print out the result or the error message

import sys


class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.calc = None
    
    def add(self):
        '''
            Add two numbers
        '''
        self.calc = self.x + self.y
    
    def sub(self):
        '''
            Subtract two numbers
        '''
        self.calc = self.x - self.y
    
    def multiply(self):
        '''
            Product of two numbers
        '''
        self.calc = self.x * self.y
    
    def division(self):
        '''
            Division of two numbers
        '''
        if self.y != 0:
            self.calc = self.x / self.y
        else:
            raise ValueError("Second number should not be zero")
            

    def print_results(self):
        '''
            Print result of operation
        '''
        print("Calculated resulted = ", self.calc)

# Solution 1 optimised solution without if block 
# def main():
#     print("A Simple Calculator")
#     number1 = float(input("Enter first number: "))
#     number2 = float(input("Enter second number: "))
#     calc = Calculator(number1, number2)
#     operations = { 1: calc.add, 2: calc.sub, 3: calc.multiply, 4: calc.division }
#     operation = int(input("Please select the operation from below:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n"))
#     if operation not in operations:
#         print("In valid option")
#         sys.exit(1)
#     operations[operation]()
#     calc.print_results()

# Solution 2 with If-else
def main():
    print("A Simple Calculator")

    # get user inputs
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    
    # intantiated Calculator object
    calc = Calculator(number1, number2)

    # get operator from the user
    operation = input("Please select any of the operations mentioned:\t+,\t-,\t*,\t/: ")

    # based on operator call the operation
    if operation == '+':
        calc.add()
    elif operation == '-':
        calc.sub()
    elif operation == '*':
        calc.multiply()
    elif operation == '/':
        calc.division()
    else:
        print("In valid option")
        sys.exit(1)
    
    # print the calculated value
    calc.print_results()


    
if __name__ == "__main__":
    main()
    
    


