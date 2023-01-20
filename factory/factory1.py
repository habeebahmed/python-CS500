from abc import ABC, abstractmethod
import enum

class Product(ABC):
	def make(self, type):
		return " is making a product " + type
		
	@abstractmethod
	def getName(self):
		pass
		

class ProductA(Product):
	def getName(self):
		return "Product A"
		
class ProductB(Product):
	def getName(self):
		return "Product B"
		
class StoreX:
	def order(self, customer, type):
		product = None
		if type == "A":
			product = ProductA()
		elif type == "B":
			product = ProductB()
			
		print("Store X -", product.make(type))
		print(customer, "ordered", product.getName(), "from Store X")
		return product
		
class StoreY:
	def order(self, customer, type):
		product = None
		if type == "A":
			product = ProductA()
		elif type == "B":
			product = ProductB()
			
		print("Store Y -", product.make(type))
		print(customer, "ordered", product.getName(), "from Store Y")
		return product	
		
		
def main():
	print("Enter a product type: ")
	type = input()
	
	store1 = StoreX()
	store1.order("Peter", type)
	store2 = StoreY()
	store2.order("Lily", type)
	
main()