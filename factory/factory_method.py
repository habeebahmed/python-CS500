from abc import ABC, abstractmethod
import enum

class Product(ABC):
	def make(self, type):
		return " is making a product " + type
		
	@abstractmethod
	def getName(self):
		pass
		
class ProductAStoreX(Product):
	def getName(self):
		return "Product A from Store X"
		
class ProductAStoreY(Product):
	def getName(self):
		return "Product A from Store Y"
		
class ProductBStoreX(Product):
	def getName(self):
		return "Product B from Store X"
		
class ProductBStoreY(Product):
	def getName(self):
		return "Product B from Store Y"
		
class Store(ABC):
	def order(self, customer, type):
		product = self.createProduct(type)
		print(product.make(type))
		print(customer, "ordered", product.getName(), "from Store X")
		return product
		
	@abstractmethod
	def createProduct(self, type):
		passs
			 
class StoreX(Store):
	def createProduct(self, type):
		product = None;
		
		if type == "A":
			product = ProductAStoreX()
		elif type == "B":
			product = ProductBStoreX()
		return product 
			
class StoreY(Store):
	def createProduct(self, type):
		product = None;
		
		if type == "A":
			product = ProductAStoreY()
		elif type == "B":
			product = ProductBStoreY()
		return product 
		
def main():
	print("Enter a product type: ")
	type = input()
	
	store1 = StoreX()
	store1.order("Peter", type)
	store2 = StoreY()
	store2.order("Lily", type)
	
main()