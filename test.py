from abc import ABC, abstractmethod, abstractproperty
from typing import List
import sys
#business classes
class Book:
    def __init__(self, isbn:str, title:str, author:str, price:float) -> None:
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__price = price

    @property
    def isbn(self)->str:
        return self.__isbn 
    @isbn.setter 
    def isbn(self,isbn)->str:
        return self.__isbn 

    @property
    def title(self)->str:
        return self.__title 
    @title.setter 
    def title(self,title)->str:
        return self.__title 
    
    @property
    def author(self)->str:
        return self.__author 
    @author.setter 
    def author(self,author)->str:
        return self.__author
    
    @property
    def price(self)->float:
        return self.__price 
    @price.setter 
    def author(self,price)->str:
        return self.__price

    def __str__(self):
        return f"Book isbn={self.__isbn}, title={self.__title}, author={self.__author}, price={self.__price:.2f}"

    def __repr__(self) -> str:
        return str(self)

    def display(self) -> None:
        print("\nISBN:",self.__isbn)
        print("Title:",self.__title)
        print("Author:",self.__author)
        print("Price:",self.__price)


class BookList:
    def __init__(self) -> None:
        self.__books: List[Book] = []
        
    def addBook(self, book):
        self.__books.append(book)
        
    def removeBook(self, book):
        self.__books.remove(book)
        
    def booksList(self)->List[Book]:
        return self.__books
    
    def inStore(self)->List[Book]:
        return self.__books

    def __str__(self) -> str:
        output = "The List Of Books\n"
        for book in self.__books:
            output += str(book) + "\n"

        return output

    def getBooksByISBN(self, isbn:str) -> Book:
        result = None
        for book in self.__books:
            if book.isbn == isbn:
                result = book
        return result

    def displayBooks(self):
        [book.display() for book in self.__books]


class OrderItem:
    def __init__(self, isbn:str, quantity:int) -> None:
        self.__isbn = isbn
        self.__quantity = quantity
        self.__orderedItems:List[Book] = []

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def quantity(self) -> int:
        return self.__quantity
    
    def __str__(self):
        return "Ordered Item Isbn: " + self.__isbn + "order "

    def display(self):
        print("ISBN:", self.__isbn)
        print("Quantity:", self.__quantity)


class Order:
    def __init__(self) -> None:
        self.__orderItems: List[OrderItem] = []

    def addItem(self, isbn, quantity):
        self.__orderItems.append(OrderItem(isbn, quantity))
    

    def getItemCount(self):
        return len(self.__orderItems)
 
    def SubmitOrderItem(self, SubmitItem:OrderItem)->None:
        print("Your order is placed!!!")
        sys.exit(0)
        
    def __str__(self):
        return "Ordered Item Isbn: " + self.__isbn + "order "
 
    def orderOrderPrice(self,order)->None:
        print(self.__orderItems)
        
    def displayOrder(self):
        for item in self.__orderItems:
            item.display()

class Invoice:
    def __init__(self, order:Order, booklist:BookList) -> None:
        self.__order = order
        self.__booklist = booklist

    def displayInvoice(self):
        if self.__order.getItemCount() == 0:
            print("There is no item in your order cart")
        else:
            self.__order.displayOrder()

        
# Command Design Pattern

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class DisplayBooklistCommand(Command):
    def __init__(self, booklist:BookList):
        self.__booklist = booklist

    def execute(self) -> None:
        self.__booklist.displayBooks()

class AddOrderItemCommand(Command):
    def __init__(self, order:Order) -> None:
        self.__order = order

    def execute(self) -> None:
        isbn = input("Enter ISBN: ")
        quantity = int(input("Enter quantity: "))
        self.__order.addItem(isbn, quantity)
        print("Total " + str(self.__order.getItemCount()) + " Item's added to cart.\n")

class ExecuteOrderItemCommand(Command):
    def __init__(self, order: Order) -> None:
        self.__order = order

    def execute(self) -> str:
        isbn = input("Enter ISBN: ")
        quantity = int(input("Enter quantity: "))
        self.__order.addItem(isbn, quantity)
        print("Total " + str(self.__order.getItemCount()) + " Item's is executed successfully.\n")
        return "Executed successfully"

class SubmitOrderItemCommand(Command):
    def __init__(self, order: Order) -> None:
        self.__order = order

    def execute(self) -> str:
        # isbn = input("Enter ISBN: ")
        # quantity = int(input("Enter quantity: "))
        #author = int(input("Enter author name:"))
        # self.__order.addItem(isbn, quantity)
        print("Total " + str(self.__order.getItemCount()) + " Item's submitted successfully for order.\n")
        return "Submitted successfully"
    

class DisplayInvoiceCommand(Command):
    def __init__(self, invoice:Invoice) -> None:
        self.__invoice = invoice

    def execute(self) -> None:
        self.__invoice.displayInvoice()


class Invoker:
    def __init__(self):
        self.__command: List[Command] = []
        
    @property
    def commands(self)->List[Command]:
        return self.commands 
    
    def add_command(self, command):
        self.__command.append(command)
        
    def remove_command(self, command):
        self.__command.append(command)

    def execute_command(self, command_no):
        return self.__command[command_no].execute()  
    
    def displayBookCommand(self, b):
        return DisplayBooklistCommand(b).execute()

    def addBookToOrder(self, o):
        return AddOrderItemCommand(o).execute()

    def removeBookToOrder(self, o):
        return RemoveOrderItemCommand(o).execute()
    
    def SubmitBookToOrder(self, o):
        return SubmitOrderItemCommand(o).execute()

    def displayInvoice(self, i):
        return DisplayInvoiceCommand(i).execute()

        
class ApplicationUserInterface:
    def __init__(self) -> None:
        self.__invoker = Invoker()

    def displayBook(self, b):
        return self.__invoker.displayBookCommand(b)

    def addItemToOrder(self, o):
        return self.__invoker.addBookToOrder(o)
    
    def removeItemToOrder(self, o):
        return self.__invoker.removeBookToOrder(o)
    
    def submitItemToOrder(self, o):
        return self.__invoker.SubmitBookToOrder(o)

    def getInvoice(self, i):
        return self.__invoker.displayInvoice(i)



# Presentation class

class BookstoreApp:
    def showTitle(self):
        print("\nThe SFBU Library Bookstore")

    def showMenu(self):
        print("==============COMMAND MENU================")
        print("1 - Display Book list")
        print("2. Add Order Item")
        print("3. Submit Order")
        #print("4. Display the Order ")
        print("4. Display Invoice")
        #print("6. Execute command")
        print("5 - Quit")



def main():
    b = BookList()
    b.addBook(Book("111", "Python", "John", 208.10))
    b.addBook(Book("112", "C++", "Peter", 108.99))
    b.addBook(Book("113", "Java", "Hobber", 318.99))
    b.addBook(Book("114", "C", "Malcom", 180.99))
    


    a = ApplicationUserInterface()
    o = Order()
    i = Invoice(o, b)

    bookstore = BookstoreApp()
    bookstore.showTitle()
    bookstore.showMenu()

    while True:
        command = input("\nCommand: ")
        if command == "1":
            a.displayBook(b)
        elif command == "2":
            a.addItemToOrder(o)
        elif command == "3":
            a.submitItemToOrder(o)
        elif command =="4":
            a.getInvoice(i)
        elif command =="5":
            print("Bye!")
            break



if __name__ == "__main__":
    main()