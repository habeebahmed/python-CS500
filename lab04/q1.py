# mypy lab04/q1.py
# ● Implement the following classes according to the class diagrams.
# ● You need to define necessary function parameters for all the classes’ constructors (...) to
# complete constructor implementations.
# ● After you implement all the classes, write a main method to create objects of the classes you
# defined and print out their contents.
# ● Each class should have appropriate setters and getters using property annotation to access
# private attributes
# ● Enhance the Order class so that it allows the main method to add and remove the order items
# from the Order instance.

class Product:
    def __init__(self, productId: int, product_name: str, price: float) -> None:
        self.__productId: int = productId
        self.__product_name: str = product_name
        self.__price: float = price

    @property
    def productId(self) -> int:
        return self.__productId

    @property
    def product_name(self) -> str:
        return self.__product_name

    @product_name.setter
    def product_name(self, product_name: str) -> None:
        self.__product_name: str = product_name

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        self.__price: float = price

    def __str__(self) -> str:
        return "Product ID = {}, Product Name = {}, Price = {}".format(self.__productId, self.__product_name, self.__price)


class Customer:
    def __init__(self, name: str, address: str) -> None:
        self.__name: str = name
        self.__address: str = address

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str) -> None:
        self.__address = address

    def __str__(self) -> str:
        return "Customer name = " + self.__name + ", address = " + self.__address


class OrderItem:
    def __init__(self, product: Product, quantity: int) -> None:
        self.__product: Product = product
        self.__quantity: int = quantity

    @property
    def product(self) -> Product:
        return self.__product

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        self.__quantity = quantity

    def total(self) -> float:
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return "Product = {}, Quantity = {}".format(self.__product, self.__quantity)


class Order:
    def __init__(self, orderId: int, customer: Customer) -> None:
        self.__orderId: int = orderId
        self.__order_items: list[OrderItem] = []
        self.__customer: Customer = customer
        self.__total: float = 0

    @property
    def customer(self) -> Customer:
        return self.__customer

    @property
    def total(self) -> float:
        self.__total: float = 0
        for item in self.__order_items:
            self.__total += (item.quantity * item.product.price)
        return self.__total

    def __str__(self) -> str:
        itemlist: str = ""
        for item in self.__order_items:
            itemlist += str(item) + "\n"
        return "Order ID = {}, Customer = {} \n{}".format(self.__orderId, self.__customer, itemlist)

    def add_item(self, product: Product, quantity: int) -> None:
        found: bool = False
        for item in self.__order_items:
            if item.product.productId == product.productId:
                item.quantity = quantity
                found = True
                break

        if found is False:
            self.__order_items.append(OrderItem(product, quantity))

    def remove_item(self, productId: int) -> None:
        index: int = next((index for (index, d) in enumerate(
            self.__order_items) if d.product.productId == productId), -1)
        if index != -1:
            self.__order_items.pop(index)

    def find_largest_item(self) -> OrderItem:
        largestItem: OrderItem = self.__order_items[0]
        for item in self.__order_items:
            if item.total() > largestItem.total():
                largestItem = item
        return largestItem

    def get_discount_value(self, discount_rate: float) -> float:
        return self.total * discount_rate

    def get_total(self) -> float:
        return self.total


def main() -> None:
    c: Customer = Customer("Peter", "San Jose")
    print(c)
    p1: Product = Product(111, 'Book', 123.43)
    p2: Product = Product(123, 'Computer', 1123.43)
    p3: Product = Product(333, 'Bag', 341.43)
    order: Order = Order(12345, c)
    order.add_item(p1, 10)
    order.add_item(p2, 10)
    order.add_item(p3, 10)
    order.add_item(p1, 20)
    order.remove_item(333)
    print(order)
    largest_item: OrderItem = order.find_largest_item()
    sub_total: float = order.get_total()
    discount: float = order.get_discount_value(0.3)
    print("Largest item\n", largest_item)
    print("\nSub-Total = ", sub_total)
    print("\nDiscount = ", discount)
    print("\nTotal = ", sub_total - discount)


if __name__ == "__main__":
    main()
