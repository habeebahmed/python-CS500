class Product:
    def __init__(self, prodcutid: int, product_name: str, price: int) -> None:
        self.__productid: int = prodcutid
        self.__product_name: str = product_name # private
        self._price: int = price # protected
        # self.test = 0 # public
    
    def display(self) -> None:
        print("productid =", self.__productid)
        print("product_name =", self.__product_name)
        print("productid =", self._price)

class Cover:
    def __init__(self, material: str) -> None:
        self.__material: str = material
    
    def display(self) -> None:
        print("material =", self.__material)

class Author:
    def __init__(self, name: str) -> None:
        self.__name: str = name

    def display(self) -> None:
        print("name =", self.__name)


class Book(Product):
    def __init__(self, prodcutid: int, product_name: str, price: int, title: str, material: str, author: Author) -> None:
        super().__init__(prodcutid, product_name, price)
        self.__title: str = title
        self.__cover: Cover = Cover(material) # Composition
        self.__author: Author = author

    def display(self) -> None:
        super().display()
        print("title =", self.__title)
        self.__cover.display()
        self.__author.display()

def main() -> None:
    author: Author = Author("Peter")
    book: Book = Book(1000, "Book", 100, "c++", "Hard Cover", author)
    book.display()

if __name__ == "__main__":
    main()