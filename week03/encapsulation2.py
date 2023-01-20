
#!/usr/bin/env python3
# encapsulation2.py

class Apple:
    def __init__(self, color, weight, price):
        self.__color = color
        self.__weight = weight
        self.__price = price
    
    @property
    def price(self):
        return self.__price
        
    @price.setter
    def price(self, price):
        self.__price = price
        
    @property
    def weight(self):
        return self.__weight  
        
    @weight.setter
    def weight(self, weight):
        self.__weight = weight
        
    @property
    def color(self):
        return self.__color  
    
    @color.setter
    def color(self, color):
        self.__color = color
    
    def __str__(self):
        return self.__color + ', ' + "{:.2f}".format(self.__weight) + ', ' + "{:.2f}".format(self.__price)

def main():
    a1 = Apple('Yellow', 0.5, 2.0)
    print("a1 =", str(a1))
    
    a1.price = 3.5
    print("a1 =", str(a1))
    
    a1.weight = 2.0
    print("a1 =", str(a1))
    
    print("a1.color =", a1.color)
    
if __name__ == "__main__":
    main()
	