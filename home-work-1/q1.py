# Question 1: 
# Create a program that, as shown in the following figures, asks the user to input the radii and centers of two circles for determining if the second circle overlaps or lies inside the first. (Hint: circle2 is inside circle1 if the distance between the two centers <= |r1 - r2| and circle2 overlaps circle1 if the distance between the two centers <= r1 + r2. Test your program to cover all cases.) 

# Enter circle1's center x-, y-coordinates, and radius: 0.5 5.1 13 
# Enter circle2's center x-, y-coordinates, and radius: 1 1.7 4.5 
# circle2 is inside circle1 
# Enter circle1's center x-, y-coordinates, and radius: 3.4 5.7 5.5 
# Enter circle2's center x-, y-coordinates, and radius: 6.7 3.5 3 
# circle2 overlaps circle1 


from math import sqrt


print("Check whether second circle overlaps or lies inside the first")
# get user input
circle_one = input("Please enter circle 1's center co-ordinates and radius: ")
circle_two = input("Please enter circle 2's center co-ordinates and radius: ")

# parse the input
circle_one_array = circle_one.split(" ")
circle_one_center_x = float(circle_one_array[0])
circle_one_center_y = float(circle_one_array[1])
circle_one_radius = float(circle_one_array[2])

circle_two_array = circle_two.split(" ")
circle_two_center_x = float(circle_two_array[0])
circle_two_center_y = float(circle_two_array[1])
circle_two_radius = float(circle_two_array[2])

# calculate distance between two centers
distance = sqrt((circle_two_center_y - circle_one_center_y)**2 + (circle_two_center_x - circle_one_center_x) ** 2)
print("Distance: ", distance)

# circle2 is inside circle1 if the distance between the two centers <= |r1 - r2|
if (distance <= abs(circle_one_radius - circle_two_radius)):
    print("circle2 is inside ciclre1")
# circle2 overlaps circle1 if the distance between the two centers <= r1 + r2
elif (distance <= abs(circle_one_radius + circle_two_radius)):
    print("circle2 overlaps ciclre1")
# if both circles are far from each other
else:
    print("both the circles are away from each other")