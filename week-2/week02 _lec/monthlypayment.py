#!/usr/bin/env python3
# display the program title
print("The Monthly Payment and Balance program")
print()

# get user inputs
amount = float(input("Enter amount of loan (e.g. 10000.00): "))
rate = float(input("Enter annual interest rate %: "))
payment = float(input("Enter monthly payment (e.g. 350.00): "))

# convert r to a monthly rate
rate /= (100 * 12)			
balance = amount

m = 1
while balance > 0.0:
	print(m, '\t', round(balance,2))
	balance += rate*balance;		# add interest to remaining balance 
	balance -= payment;				# subtract monthly payment
	m += 1
	
print()
print('Bye!')