#!/usr/bin/env python3

# display the program title
print("The Letter Grade Calculator")
print()

# get user input
score = int(input("Enter score (0-100): "));        

if score >= 90:	   
	grade = 'A'	   
elif score >= 80:	   
	grade = 'B'	   
elif score >= 70:	   
	grade = 'C'	   
elif score >= 60:	   
	grade = 'D'	   
else:   
	grade = 'F'	
	
# display the result
print("The grade is: " + grade)
print() 
print("Bye")