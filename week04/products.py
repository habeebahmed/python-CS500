class Product:
    def __init__(self, product_name = "", price = 0.0, rebate = 0.0, warranty = 1):
        self.__product_name = product_name
        self.__price = price
        self.__rebate = rebate
        self.__warranty = warranty

    @property
    def product_name(self):
        return self.__product_name
        
    @property
    def price(self):
        return self.__price
        
    @price.setter
    def price(self, price):
        self.__price = price
        
    @property
    def rebate(self):
        return self.__rebate
        
    @rebate.setter
    def rebate(self, rebate):
        self.__rebate = rebate
        
    @property
    def warranty(self):
        return self.__warranty
        
    def calculate_cash_rebate(self):
        return self.price * self.__rebate / 100

    def calculate_price(self):
        return self.price - self.calculate_cash_rebate()

    def display(self):
        print("Product name:", self.__product_name)
        print("Price:", self.__price)
        print("Rebate:", self.__rebate)
        print("Warranty:", self.__warranty)
    
class Computer(Product):
    def __init__(self, computer_type, product_name = "", price = 0.0, rebate = 0.0, warranty = 1):
        Product.__init__(self, product_name, price, rebate, warranty)
        self.__computer_type = computer_type

    @property
    def computer_type(self):
        return self.__computer_type
        
    def display(self):
        Product.display(self)
        print("Computer type:", self.__computer_type)
                
class Car(Product):
    def __init__(self, horsepower, product_name = "", price = 0.0, rebate = 0.0, warranty = 1):
        Product.__init__(self, product_name, price, rebate, warranty)
        self.__horsepower = horsepower
        
    @property
    def horsepower(self):
        return self.__horsepower
        
    def display(self):
        Product.display(self)
        print("Horsepower:", self.__horsepower)
 
def main():
    products = []
    products.append(Computer("Desktop", "Computer", 1000.00, 12.5, 2))
    products.append(Car(300.0, "Car", 50000.00, 0.5, 5))
    
    for product in products:
        product.display()
        print()
        
if __name__ == "__main__":
    main()