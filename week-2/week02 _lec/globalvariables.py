#!/usr/bin/env python3

PI = 3.14			# Global Constant 
sum = 0				# Gloabl Variable

def calSum(x, y):
	sum = x + y
	return sum
	
def calSum2(x, y):
	global sum
	sum = x + y
	return sum
	
def printSum():
	global sum
	print('global sum =', sum, '\n')
	
def getArea(radius):
	return radius * radius * PI
	
def main():
	print("The Demo Program for Global Variables\n")
	
	total = calSum(10, 20)
	print('calSum(10, 20) =', total)
	printSum()
	
	total = calSum2(10, 20)
	print('calSum2(10, 20) =', total)
	printSum()
	
	area = getArea(8)
	print('getArea(10) =', round(area,2), '\n')
	
	print("Bye!")
	
if __name__ == "__main__":
	main()