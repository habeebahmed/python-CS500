import csv
from business import Book

class BookRepository:
	def __init__(self) -> None:
		self.__FILENAME = "books.csv"

	def get_books(self) -> dict[str, Book]:
		books = {}
		with open(self.__FILENAME, newline = "") as file:
			reader = csv.reader(file)
			for row in reader:
				# convert row to Book object
				book = Book(row[0], row[1], row[2], float(row[3])) 
				books[row[0]] = book
		return books
