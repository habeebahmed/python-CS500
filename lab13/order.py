import sys
from abc import ABC, abstractmethod
from typing import List


class Book:
    def __init__(self, isbn: str, title: str, author: str, price: float) -> None:
        self.__isbn: str = isbn
        self.__title: str = title
        self.__author: str = author
        self.__price: float = price
    
    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def title(self) -> str:
        return self.__title

    @property
    def price(self) -> float:
        return self.__price

    def __str__(self) -> str:
        return f"Book isbn={self.__isbn}, title={self.__title}, author={self.__author}, price={self.__price}"

    def __repr__(self) -> str:
        return str(self)

class BookList:
    def __init__(self) -> None:
        self.__books: list[Book] = []

    def __str__(self) -> str:
        output = "The List of Books\n"
        for book in self.__books:
            output += str(book) + "\n"
        
        return output

    def add_book(self, book: Book) -> None:
        self.__books.append(book)

    def get_book_isbn(self, isbn: str):
        try:
            obj: Book = next(book for book in self.__books if book.isbn == isbn)
        except Exception as e:
            print(f"{e}")
            return None
        
        return obj

class OrderItem:
    def __init__(self, isbn: str, quantity: int) -> None:
        self.__isbn = isbn
        self.__quantity = quantity
    
    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def quantity(self) -> int:
        return self.__quantity

class Order:
    def __init__(self) -> None:
        self.__orderitems: list[OrderItem] = []

    def add_item(self, isbn: str, quantity: int) -> None:
        self.__orderitems.append(OrderItem(isbn, quantity))
    
    def get_order_items(self) -> List[OrderItem]:
        return self.__orderitems

class Invoice:
    def __init__(self, order: Order, booklist: BookList) -> None:
        self.__order: Order = order
        self.__booklist: BookList = booklist

    def generate_invoice(self) -> str:
        invoice_str: str = "========Invoice details=========\n"

        order_items: List[OrderItem] = self.__order.get_order_items()

        if not order_items:
            return invoice_str+ "-----No Items------"
        
        for order in order_items:
            book: Book | None = self.__booklist.get_book_isbn(order.isbn)
            if book:
                invoice_str += f"Book={book.title} Price={book.price} Quantity={order.quantity} => Item total = {book.price * order.quantity}\n4"

        return invoice_str


class Command(ABC):
    @abstractmethod
    def execute(self) -> str:
        pass

class DisplayBookListCommand(Command):
    def __init__(self, booklist: BookList) -> None:
        self.__booklist: BookList = booklist

    def execute(self) -> str:
        return str(self.__booklist)

class AddOrderItemCommand(Command):
    def __init__(self, order: Order, booklist: BookList) -> None:
        self.__order: Order = order
        self.__booklist: BookList = booklist
    
    def execute(self):
        isbn: str = input("Enter ISBN: ")
        quantity: int = int(input("Enter quantity: "))
        if not self.__booklist.get_book_isbn(isbn):
            return "The ISBN entered does not exists"
        self.__order.add_item(isbn, quantity)
        return "Added successfully"

class RemoveOrderItemCommand(Command):
    pass

class SubmitOrderCommand(Command):
    def __init__(self, order: Order, booklist: BookList) -> None:
        self.__order: Order = order
        self.__booklist: BookList = booklist
    def execute(self) -> str:
        order_items: List[OrderItem] = self.__order.get_order_items()
        total = 0

        if not order_items:
            return ""
        
        for order in order_items:
            book: Book | None = self.__booklist.get_book_isbn(order.isbn)
            if book:
                total += book.price * order.quantity
        return f"\n\nOrder submitted successfully\nThe total is {total}"

class DisplayInvoiceCommand(Command):
    def __init__(self, invoice: Invoice) -> None:
        self.__invoice = invoice

    def execute(self):
        return self.__invoice.generate_invoice()

class ExitCommand(Command):
    def execute(self) -> str:
        sys.exit(0)
        return "Exiting....."


class Invoker:
    def __init__(self) -> None:
        self.__command: list[Command] = []

    def add_command(self, command: Command) -> None:
        self.__command.append(command)

    def execute_command(self, command_no: int) -> str:
        return self.__command[command_no].execute()

def show_menu():
    print("===== Menu =========")
    print("1. Display Book List")
    print("2. Add Order Item")
    print("3. Display Invoice")
    print("4. Submit Order")
    print("5. Exit")

def process_command(choice: int, invoker: Invoker):
    print(invoker.execute_command(choice - 1))

def main() -> None:
    b1: Book = Book("111", "C Programming", "Peter", 122.89)
    b2: Book = Book("222", "C++ Programming", "Peter", 132.89)
    booklist: BookList = BookList()
    booklist.add_book(b1)
    booklist.add_book(b2)


    order: Order = Order()
    invoice: Invoice = Invoice(order, booklist)
    invoker: Invoker = Invoker()
    invoker.add_command(DisplayBookListCommand(booklist))
    invoker.add_command(AddOrderItemCommand(order, booklist))
    invoker.add_command(DisplayInvoiceCommand(invoice))
    invoker.add_command(SubmitOrderCommand(order, booklist))
    invoker.add_command(ExitCommand())

    while True:
        show_menu()
        choice: int = int(input("Please ‘enter your choice: "))
        process_command(choice, invoker)

if __name__=="__main__":
    main()