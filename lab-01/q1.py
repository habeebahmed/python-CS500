# Write a program that sums a sequence of product prices. 
# Assume that the first value read is an integer that specifies the number of prices remaining to be entered. 
# Your program should read all the values in one line. A typical input sequence might be
# 5 107.55 200.5656 304.55 400.33 511.33545
# where the 5 indicates that the subsequent 5 prices are to be summed. The sum is $1,524.33

print("Calculating the sum of product prices")

# get user input
user_input = input("Please enter values ")

# split the received input by space into array
arr = user_input.split(' ')

# initiate sum and counter
sum = 0
n = 0

# loop through the array until 'n' reaches the first value of array which is number of prices 
while n < int(arr[0]):
# increment counter
    n += 1
# skip the first element since it's number of prices
    if (n == 0):
        continue
# Accumulate to the sum variable 
    sum += int(arr[n])

print("The sum is: ", sum)