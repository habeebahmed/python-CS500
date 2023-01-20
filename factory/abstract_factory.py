from abc import ABC, abstractmethod
import enum

class Component(ABC):
	@abstractmethod
	def getComponent(self):
		pass
	
class ComponentStoreX(Component):
	def getComponent(self):
		return "Component for Store X"
		
class ComponentStoreY(Component):
	def getComponent(self):
	    return "Component for Store Y"

class ComponentFactory(ABC):
	@abstractmethod
	def createComponent(self):
		pass
	
class ComponentFactoryStoreX(ComponentFactory):
	def createComponent(self):
		return ComponentStoreX()
		
class ComponentFactoryStoreY(ComponentFactory):
	def createComponent(self):
		return ComponentStoreY()
		
class Product(ABC):
	def __init__(self):
		self.factory = None
		self.component = None
		
	def make(self, type):
		return "Making a " + self.getName() + " with " + self.component.getComponent()
		
	@abstractmethod
	def getName(self):
		pass
		
class ProductA(Product):
	def __init__(self, factory):
		self.factory = factory
		self.component = factory.createComponent()
		
	def getName(self):
		return "Product A"
		
class ProductB(Product):
	def __init__(self, factory):
		self.factory = factory
		self.component = factory.createComponent()
		
	def getName(self):
		return "Product B"
		
class Store(ABC):
	def __init__(self):
		self.factory = None
		
	def order(self, customer, type):
		product = self.createProduct(type)
		print(product.make(type))
		print(customer, "ordered", product.getName())
		return product
		
	@abstractmethod
	def createProduct(self, type):
		passs
			 
class StoreX(Store):
	def createProduct(self, type):
		factory = ComponentFactoryStoreX()
		product = None;
		
		if type == "A":
			product = ProductA(factory)
		elif type == "B":
			product = ProductB(factory)
		return product 
			
class StoreY(Store):
	def createProduct(self, type):
		factory = ComponentFactoryStoreY()
		product = None;
		
		if type == "A":
			product = ProductA(factory)
		elif type == "B":
			product = ProductB(factory)
		return product 
		
def main():
	print("Enter a product type: ")
	type = input()
	
	store1 = StoreX()
	store1.order("Peter", type)
	store2 = StoreY()
	store2.order("Lily", type)
	
main()