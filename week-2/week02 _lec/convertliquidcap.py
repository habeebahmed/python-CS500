import unitconverters as converter

def displayMenu():
	print("The Convert Liquid Capacity Program")
	print()
	print("MENU")
	print("1. Gallon to Liter")
	print("2. Liter to Gallon")
	print()

def convertLiquidCap():
	option = int(input("Enter a menu option: "))
	if option == 1:
		g = float(input("Enter gallons: "))
		l = converter.toLiter(g)
		l = round(l, 2)
		print("Liters:", l)    
	elif option == 2:
		l = float(input("Enter liters: "))
		g = converter.toGallon(l)
		g = round(g, 2)
		print("Gallons:", g)
	else:
		print("You enterred an invalid menu number.")

def main():
	displayMenu()
	again = "y"
	while again.lower() == "y":
		convertLiquidCap()
		print()
		again = input("Convert another liquid capacity unit? (y/n): ")
		print()
	print("Bye!")

if __name__ == "__main__":
	main()
	
