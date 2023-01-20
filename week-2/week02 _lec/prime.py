#!/usr/bin/env python3
# display the program title

print("Find the prime numbers from 2 to 20")
print()

for i in range(2,20):
	isPrime = True
	for j in range(2, i // 2 + 1):
		if i % j == 0:
			isPrime = False
			break
	if isPrime == True:
		print(i, "is prime")
	
print()
print('Bye!')