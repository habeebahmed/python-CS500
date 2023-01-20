class Book:
	# a constructor that initializes 3 attributes
	def __init__(self, title, author="", price=0.0):                   
		self.__title = title        
		self.__author = author
		self.price = price
	
	# a method that get the book title
	def getTitle(self):
		return self.title
	
	# a method that sets the book title
	def setTitle(self, title):
		self.__title = title
		
	# a method that get the book author
	def getTitle(self):
		return self.author
	
	# a method that sets the book author
	def setAuthor(self, author):
		self.__author = author
	
	def __str__(self):
		return self.__title + ","  + str(self.__author) + "," + str(self.price)