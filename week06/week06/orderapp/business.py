from __future__ import annotations

class Book:
	def __init__(self, isbn: str = "", title: str = "", author: str = "", price: float = 0.0) -> None:
		self.__isbn = isbn
		self.__title = title
		self.__author = author
		self.__price = price
		
	@property
	def isbn(self) -> str:
		return self.__isbn
		
	@property
	def title(self) -> str:
		return self.__title
		
	@property
	def author(self) -> str:
		return self.__author
	
	@property
	def price(self) -> float:
		return self.__price
		
	@price.setter
	def price(self, price: float) -> None:
		self.__price = price
		
	def get_discount_amount(self, quantity: int) -> float:
		discount_percent = 0.0
		
		if quantity > 50:
			discount_percent = 10	# 10% discount over 50
		elif quantity > 200:
			discount_percent = 20	# 20% discount over 200
			
		discount_amount = self.__price * discount_percent / 100
		return round(discount_amount, 2)
	
	def get_discount_price(self, quantity: int) -> float:
		discount_price = self.__price - self.get_discount_amount(quantity)
		return round(discount_price, 2)
		
	def display(self) -> None:
		print('ISBN =', self.__isbn)
		print('Title =', self.__title)
		print('Author =', self.__author)
		print('Price =', self.__price)
		

class OrderItem:
	def __init__(self, book: Book, quantity: int = 1) -> None:
		self.__book = book
		self.__quantity = quantity
		
	@property
	def book(self) -> Book:
		return self.__book
	
	@property
	def quantity(self) -> int:
		return self.__quantity	
	
	def get_total(self) -> float:
		total = self.__book.get_discount_price(self.__quantity) * self.__quantity
		return total

	def display(self) -> None:
		self.__book.display()
		print('Quantity =', self.__quantity)
		print('Discount Price =', self.__book.get_discount_price(self.__quantity))
		print('Item Total =', self.get_total())
		
class Order:
	def __init__(self) -> None:
		self.__orderItems: list[OrderItem] = []
	
	def add_item(self, item: OrderItem) -> None:
		self.__orderItems.append(item)
	
	def remove_item(self, index: int) -> None:
		self.__orderItems.pop(index)
	
	def get_total(self) -> float:
		total = 0.0
		for item in self.__orderItems:
			total += item.get_total()
		return total
	
	def get_item_count(self) -> int:
		return len(self.__orderItems)
	
	def __iter__(self) -> Order:
		self.__index = -1
		return self
	
	def __next__(self) -> OrderItem:
		if self.__index == len(self.__orderItems)-1:
			raise StopIteration         
		self.__index += 1
		orderItems = self.__orderItems[self.__index]
		return orderItems
		
	def display(self) -> None:
		for item in self:
			item.display()
			print()
			
		print("Order Total =", self.get_total())
