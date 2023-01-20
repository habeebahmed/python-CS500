#!/usr/bin/env python3

import random

LIMIT = 100

# get a random numbe form 1 to 100
magic = random.randint(1, LIMIT)
count = 0

while True:
	guess = int(input("Enter your guess (1 to 100): "))
	if guess < magic:
		print("Too low.")
		count += 1
	elif guess > magic:
		print("Too high.")
		count += 1
	elif guess == magic:
		print("You guessed it in " + str(count) + " tries.\n")
		break;
print('bye!')