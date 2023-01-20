#!/usr/bin/env python3
# colleges.py

# create a college
college = []

# create three courses
java_course = []
java_course.append("Java Programming")
java_course.append("Henry")
java_course.append("3")
java_course.append("Tuesdays")

python_course = []
python_course.append("Python Programming")
python_course.append("Peter")
python_course.append("3")
python_course.append("Wednesdays")

network_course = []
network_course.append("Network Fundamental")
network_course.append("Chester")
network_course.append("3")
network_course.append("Mondays")

# add courses to college
college.append(java_course)
college.append(python_course)
college.append(network_course)

print(college)

# print the list of lists as a 2-D list
for program in college:
    for item in program:
        print(item, end=',')
    print()
    
print()
# print the list of lists as a 2-D list using indexes
row = 0
col = 0
while row < len(college):
    while col < len(college[row]):
        print(college[row][col], end=',')
        col += 1
    print()
    col = 0
    row += 1
    