#!/usr/bin/env python3
# composition.py

import random

colors = ["Green", "Red", "Yellow"]

class Apple:
    def __init__(self, color, weight, price):
        self.color = color
        self.weight = weight
        self.price = price
    
    def change_color(self):
        clr = random.randint(0,2)
        self.color = colors[clr]
    
    def __str__(self):
        return self.color + ', ' + "{:.2f}".format(self.weight) + ', ' + "{:.2f}".format(self.price)


class Barrel:
    def __init__(self):
        self.list = []
    
    def add_apple(self, apple):
        self.list.append(apple)
    
    def change_all_colors(self):
        for apple in self.list:
            apple.change_color()
    
    def displayall(self):
        for apple in self.list:
            print(str(apple))			

def main():
    a1 = Apple('Yellow', 0.5, 2.0)
    a2 = Apple('Green', 0.56, 2.5)
    a3 = Apple('Red', 1.2, 3.5)
    
    barrel = Barrel()
    barrel.add_apple(a1)	
    barrel.add_apple(a2)	
    barrel.add_apple(a3)
    barrel.displayall()
    
    print('\nAfter color changed:')
    barrel.change_all_colors()
    barrel.displayall() 

    

if __name__ == "__main__":
    main()
	