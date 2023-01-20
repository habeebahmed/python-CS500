#!/usr/bin/env python3

def calculateSavings(initialDepositAmount, annualInterestRate, years):
	# convert annual interest rate to monthly interest rates
	monthlyInterestRate = annualInterestRate / 12 / 100
	months = years * 12

	# calculate the future value
	estimatedBalance = initialDepositAmount
	for i in range(months):
		monthlyInterestAmount = estimatedBalance * monthlyInterestRate
		estimatedBalance = estimatedBalance + monthlyInterestAmount		
	return estimatedBalance
	
def main():
	print("The Simple Savings Calculator using Functions")
	print()
	
	confirm = "y"
	while confirm.lower() == "y":	
		# get inputs from the keyboard
		initialDepositAmount = float(input("Enter initial deposit amount:\t"))
		annualInterestRate = float(input("Enter annual interest rate:\t"))
		years = int(input("Enter number of years:\t\t"))
		
		# get the estimated balance
		estimatedBalance = calculateSavings(initialDepositAmount, annualInterestRate, years)
		
		# format and display the result
		print("Estimated Balance:\t\t" + "{:.2f}".format(estimatedBalance))
		print()		
		# see if the user wants to continue
		confirm = input("Continue? (y/n): ")
		print()
	
	print("Bye!")
	
if __name__ == "__main__":
	main()