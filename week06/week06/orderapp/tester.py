from db import BookRepository
from business import Book, OrderItem, Order

def main() -> None:
	order = Order()
	db = BookRepository()

	books = db.get_books()
	book = books["2222"]
	orderItem = OrderItem(book, 250)
	order.add_item(orderItem)
	
	book = books["3333"]
	orderItem = OrderItem(book, 70)
	order.add_item(orderItem)
	
	order.display()	
	
if __name__ == "__main__":
	main()
	

	