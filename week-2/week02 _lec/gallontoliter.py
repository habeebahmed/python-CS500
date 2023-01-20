#!/usr/bin/env python3

# display the program title
print("The Gallons to Liters Program")
print()

# get input from the user
gallons = float(input("Enter number of gallons:\t"))

# convert to liters
liters = gallons * 3.7854
liters = round(liters, 2)
            
# format and display the result
print()
print("Liters:\t\t\t\t" + str(liters))
print()
print("Bye")