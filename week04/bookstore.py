class Book:
    def __init__(self, title, author, price = 0.0):
        self.__title = title
        self.__author = author
        self.__price = price

    @property  # read-only!
    def title(self):
        return self.__title
        
    @property  # read-only!
    def author(self):
        return self.__author
        
    @property 
    def price(self):
        return self.__price;
        
    @price.setter
    def price(self, price):
        self.__price = price;
    
    def display(self):
        print('Title:', self.__title)
        print('Author:', self.__author)
        print('Price:', "{:.2f}".format(self.__price))

    def __str__(self):
        return self.__title + ', ' + self.__author + ', ' + "{:.2f}".format(self.__price) 
                
class Bookstore:
    def __init__(self, store_name):
        self.__list = []
        self.__store_name = store_name

    def add_book(self, book):
        self.__list.append(book)
                
    def displayall(self):
        for book in self.__list:
            book.display()
            
    # define the Book object as the iterator
    def __iter__(self):
        self.__index = -1   # initialize index for each iteration
        return self

    # define the method that gets the next object    
    def __next__(self):
        if self.__index >= len(self.__list)-1:
            raise StopIteration()
        self.__index += 1
        book = self.__list[self.__index]
        return book

def main():
    b1 = Book('C++', 'Henry', 78.8)
    b2 = Book('Java', 'Sandy', 68.8)
    b3 = Book('PHP', 'Peter', 58.8)
    
    bookstore = Bookstore('NPU bookstore')
    bookstore.add_book(b1)
    bookstore.add_book(b2)
    bookstore.add_book(b3)
    
    for book in bookstore:
        print(book)
    
if __name__ == "__main__":
    main()