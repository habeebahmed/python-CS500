#!/usr/bin/env python3

# display the program title
print("The Test Scores program")
print()

print("Enter 911 to end input")

# initialize variables
numScores = 0
totalScore = 0
testScore = 0

while True:
    testScore = int(input("Enter test score: "))
    if testScore >= 0 and testScore <= 100:
        totalScore += testScore
        numScores += 1
    elif testScore == 911:
        break
    else:
        print("Test score must be from 0 through 100."
              + "Score discarded. Try again.")

# calculate average score
if numScores > 0:
	averageScore = round(totalScore / numScores, 2)
else:
	averageScore = 0.0
                
# format and display the result
print("======================")
print("Total Score:", totalScore, "\nAverage Score:", averageScore)
print()
print("Bye")


