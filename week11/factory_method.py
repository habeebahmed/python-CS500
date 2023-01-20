class Product:
    def do_something(self):
        pass
    def modify_something(self):
        pass

class Website(Product):
    pass

class Building(Product):
    pass

class Company:
    def do_business(self, type):
        product = self.create_product()
        product.do_something()
        product.modify_something()

    # factory method
    def create_product(self):
        pass

class InternetCompany(Company):
    def create_product(self):
        return Website()

class ConstructionCompany(Company):
    def create_product(self):
        return Building()
    