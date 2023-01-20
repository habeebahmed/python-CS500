#!/usr/bin/env python3
# display the program title
print("The Notice program")
print()

# get user inputs
studentID = int(input("Enter a Student ID number: "))
test1 = int(input("Enter first score (0-100): "))
test2 = int(input("Enter first score (0-100): "))
test3 = int(input("Enter first score (0-100): "))

print()
print("Student number: ", studentID)
print("Test Scores: ", test1, test2, test3)

# calculate the average of three test grades and 
# determine whether or not the student is passing
if test1 < 0 or test2 < 0 or test3 < 0:
	dataOK = 0
else:
	dataOK = 1

if dataOK:
	average = (test1 + test2 + test3) / 3
	print("Average Score is : ", round(average,2))
	
	if average >= 60.0:
		notice = "Passing"
		if average < 70.0:
			notice += " but marginal"
		print(notice + ".")
	else:
		print("Failing.")
else:
	print("Invalid Data: Scores(s) less than zero.\n")
	
print() 
print("Bye")