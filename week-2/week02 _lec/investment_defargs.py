#!/usr/bin/env python3

def calculateSavings(initialDepositAmount, annualInterestRate=2.0, years = 10):
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
	print("The Simple Savings Calculator using default arguments and named arguments")
	print()
	
	# using default arguments
	estimatedBalance = calculateSavings(10000, 2.0, 10)
	print("calculateSavings(10000, 2.0, 10):\t" + "{:.2f}".format(estimatedBalance))
	
	estimatedBalance = calculateSavings(10000, 2.0)
	print("calculateSavings(10000, 2.0):\t\t" + "{:.2f}".format(estimatedBalance))
	
	estimatedBalance = calculateSavings(10000)
	print("calculateSavings(10000):\t\t" + "{:.2f}".format(estimatedBalance))
	
	estimatedBalance = calculateSavings(annualInterestRate=5.0, years=30, initialDepositAmount=20000)
	print("calculateSavings(annualInterestRate=5.0, years=30, initialDepositAmount=20000):\t" + "{:.2f}".format(estimatedBalance))
	
	print()		
	print("Bye!")
	
if __name__ == "__main__":
	main()