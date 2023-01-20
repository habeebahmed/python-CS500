from bookstore import Book, Bookstore

def main():
    print("The Bookstore test program")
    print()
    bookstore = Bookstore("NPU bookstore")
    
    # get books from user
    while True:
        print("Enter a book information: ")
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        price = float(input("Enter book price: "))
        
        bookstore.addBook(Book(title, author, price))

        print()
        choice = input("Do you want to add another book? (y/n): ")
        if choice != "y":
            print("Bye!")
            break
        print()
        
    print()    
    print("The bookstore has the following books now.")
    for book in bookstore:
        book.display()
        print()

if __name__ == "__main__":
    main()
 