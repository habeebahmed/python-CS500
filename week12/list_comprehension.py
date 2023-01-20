from functools import reduce

# https://drive.google.com/file/d/1XhbfzOnZJA4-Vw0TxmPpypXBUt8qEDMx/view

# Q1
from typing import List


degreesInCelsius = [0, 10, 12, 13, 14, 21, 15, 32]

degreesInFahrenheit = [round((9/5) * tempC + 32, 1)
                       for tempC in degreesInCelsius]

print(degreesInFahrenheit)

# Q2
# limit = int(input("Please enter a number upto 100: "))
# multiples = [ i for i in range(limit, 101, limit)]

# print(multiples)


# Q3

q3_list = [2, 4, 5, 10, 12, 15, 30]

list_divisible_by_five = [x for x in q3_list if x % 5 == 0]

print(list_divisible_by_five)


# Q4
# temp_c = float(input("Please enter temperature in Celsius: "))

# temp_f: float = (lambda x: float: round((9/5) * x + 32, 1))(temp_c)

# print(temp_f)


# Q5

names = [" Peter", " Nancy ", "Paul ", " Thomas "]
names_trimmed = list(map(lambda x: x.strip(), names))

print(names_trimmed)


# Q6

names = ['Peter', 'Nancy', 'Paul', 'Thomas']
names_filtered: List[str] = list(filter(lambda x: x[0] == 'P', names))

print(names_filtered)


fruits = ["apple", "orange", "pear", "banana"] 

def capitalize_fruits(a: str, b: str):
    c = ""
    if a != "":
        c = a + ", " + b.capitalize()
    else:
        c = b.capitalize()
    return c

fruits_appended = reduce(lambda prev, next:  prev + ", " + next.capitalize() if prev != "" else next.capitalize(), fruits, "")

print(fruits_appended)
