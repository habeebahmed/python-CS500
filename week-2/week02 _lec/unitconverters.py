""" 
This module contains functions for converting liquid capacity 
between gallons and degrees liters
"""

def toLiter(gallons):
	"""
	Accepts gallons and returns liters  
	"""
	liters = gallons * 3.785411784
	return liters

def toGallon(liters):
	"""
	Accepts liters and returns gallons 
	"""
	gallons = liters * 0.2641720524
	return gallons
	
def main():
	print("1 gallon =", toLiter(1), "liters")
	print("1 liter =", toGallon(1), "gallons")
	
if __name__ == "__main__":
	main()
	
