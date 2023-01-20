# Write a Python program to calculate the area of simple shapes. First of all, create 3 functions: 
# ● def getRectangleArea(length, width): 
    # ○ # Calculate the area as length * width and then return the result. 
# ● def getTriangleArea(length, width): 
    # ○ # Calculate the area as base * height / 2 and then return the result. 
# ● def getCircleArea(radius): 
    # ○ # Calculate the area as radius * radius * 3.14 and then return the result. 
# The algorithm would be: 
# 1. Get the shape desired. 
# 2. If the shape is a rectangle 
    # a. Get length and width 
    # b. Call getRectangleArea() 
# 3. If the shape is a right triangle, 
    # a. Get the base and height 
    # b. Call getTriangleArea() 
# 4. If the shape is a circle 
    # a. Get the radius 
    # b. Call getCircleArea() 
# 5. Print out the area.

import sys


def getRectangleArea(length, width): 
    return length * width
def getTriangleArea(base, height): 
    return 0.5 * base * height
def getCircleArea(radius):
    return 3.14 * radius * radius

def main():
    print("Calculate the area of simple shapes")

    # get the shape desired
    shape = input("Please enter the shape: ")
    
    area = 0
    # base on shape calculate area
    if shape == 'rectangle':
        length = float(input("Please enter length of rectangle: "))
        width = float(input("Please enter width of rectangle: "))
        area = getRectangleArea(length, width)
    elif shape == 'triangle':
        base = float(input("Please enter base of triangle: "))
        height = float(input("Please enter height of triangle: "))
        area = getTriangleArea(base, height)
    elif shape == 'circle':
        radius = float(input("Please enter radius of circle: "))
        area = getCircleArea(radius)
    else:
        print("In valid option")
        sys.exit(1)
    
    # print area
    print("Area of {} is {}".format(shape, area))

if __name__ == "__main__":
    main()