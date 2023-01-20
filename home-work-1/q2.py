# You will frequently be requested to calculate the mean and standard deviation of data in business applications. Simple terms, the mean is the average of the numbers. The standard deviation is a statistic that reveals how closely all the different variables in a set of data are clustered around the mean. What, for instance, is the typical age of a class of students? How close are the ages? The deviation is zero if the students are of the same age. Create a program that asks the user to enter ten values and then uses the formula below to display the mean and standard deviation of those numbers: 
# Here is a sample run: 
# Enter ten numbers: 1 2 3 4.5 5.6 6 7 8 9 10 
# The mean is 5.61 
# The standard deviation is 2.99794 


from math import sqrt
import sys
print("Calculate Mean and Standard deviation ")

# Get user input

list_of_var = input("Enter ten numbers: ")
list_of_var_float = list(map(float, list_of_var.split(" ")))

if not bool(list_of_var_float) or len(list_of_var_float) > 10:
    print("Please enter only 10 values")
    sys.exit(1)

# mean
sum_of_numbers = 0
for var in list_of_var_float:
    sum_of_numbers += var

mean_nums = sum_of_numbers / len(list_of_var_float)

print("The mean is:  ", mean_nums)

# standard deviation
sd_num = 0
for x in list_of_var_float:
    sd_num += (x - mean_nums) ** 2

sd = sqrt(sd_num / (len(list_of_var_float) - 1))

print("The standard deviation is: ", sd)