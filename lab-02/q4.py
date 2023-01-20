# Given as input two whole numbers representing a time like time, minute. Additional input is a time shift in minutes. Print the time prior to a time shift and the time following the time shift. Assume that the four is in 24hr format. 
# Find the time x minutes before and after the input time 
# Enter a time (hh:mm): 23:55 
# Enter a time shift in mins: 10 
# 23:45 
# 00:05 

import sys


print("Find the time x minutes before and after the input time")

# Get user input in hh:mm format
timeString = input("Enter the time string: ")
shiftMins = int(input("Enter the time shift in minutes: "))
timeArray = timeString.split(':')
hours = int(timeArray[0])
mins = int(timeArray[1])

# check valid time string
if not bool(timeArray[0]) or not bool(timeArray[1]):
    print("Invalid time string")
    sys.exit()

# calculate time before shift mins
totalMins = hours * 60 + mins
timeBeforeInMins = totalMins - shiftMins
hoursBefore = timeBeforeInMins // 60 % 24
minsBefore = timeBeforeInMins % 60
print("Before: {0:02d}:{1:02d}".format(hoursBefore, minsBefore))

# calculate time after shift mins
timeAfterInMins = totalMins + shiftMins
hoursAfter = timeAfterInMins // 60 % 24
minsAfter = timeAfterInMins % 60
print("After: {0:02d}:{1:02d}".format(hoursAfter, minsAfter))