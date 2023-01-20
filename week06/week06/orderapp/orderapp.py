from db import BookRepository
from business import Book, OrderItem, Order

class OrderApp:
	def __init__(self) -> None:
		bookdb = BookRepository()
		self.__books = bookdb.get_books()
		self.__order = Order()
		
	def show_title(self) -> None:
		print("The Bookstore program")
		print()
    
	def show_menu(self) -> None:
		print("COMMAND MENU")
		print("order - Show the order")
		print("add  - Add an item to the order")
		print("del  - Delete an item from order")
		print("exit - Exit program")
		print()

	def show_books(self) -> None:
		print("BOOKS")
		lineFormat1 = "{:<5s} {:<25s} {:>25s} {:>10s}"
		lineFormat2 = "{:<5s} {:<25s} {:>25s} {:>10.2f}"
		print(lineFormat1.format("ISBN", "Title", "Author", "Price"))
		for isbn, book in self.__books.items():
			print(lineFormat2.format(book.isbn,
			book.title,
			book.author,
			book.price))
		print()

	def show_order(self) -> None:
		if self.__order.get_item_count() == 0:
			print("There are no items in your order.\n")
		else:
			# items = order.lineItems
			line_format1 = "{:<5s} {:<5s} {:<25s} {:>12s} {:>10s} {:>10s}"
			line_format2 = "{:<5d} {:<5s} {:<25s} {:>12.2f} {:>10d} {:>10.2f}"
			print(line_format1.format("Item", "ISBN", "Title", "Your Price",
									  "Quantity", "Total"))
			i = 0
			for item in self.__order:
				print(line_format2.format(i + 1,
					item.book.isbn,
					item.book.title,
					item.book.get_discount_price(item.quantity),
					item.quantity,
					item.get_total()))
				i += 1
			print("{:>66.2f}".format(self.__order.get_total()))
			print()


	def add_item(self) -> None:
		isbn = input("ISBN: ")
		quantity = int(input("Quantity: "))
		if isbn not in self.__books:
			print("No book has that isbn.\n")
		else:
			# Get Book object, store in OrderItem object,
			# and add to Order object
			book = self.__books[isbn]
			item = OrderItem(book, quantity)
			self.__order.add_item(item)
			print("Item " + str(self.__order.get_item_count()) + " was added.\n")

	def remove_item(self) -> None:
		itemNo = int(input("Item No: "))
		if itemNo < 1 or itemNo > self.__order.get_item_count():
			print("The cart does not contain an item " +
				"with that item number.\n")
		else:
			# Remove LineItem object at specified index from cart
			self.__order.remove_item(itemNo-1)
			print("Item " + str(itemNo) + " was deleted.\n")   


def main() -> None:
	app = OrderApp()
	app.show_title()
	app.show_menu()
	# display Book objects
	app.show_books()

	while True:        
		command = input("Command: ")
		if command == "order":
			app.show_order()
		elif command == "add":
			app.add_item()
		elif command == "del":
			app.remove_item()
		elif command == "exit":
			print("Bye!")
			break
		else:
			print("Not a valid command. Please try again.\n")


if __name__ == "__main__":
	main()

