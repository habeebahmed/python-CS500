from market import Apple, Barrel

def main():
    print("The Market Test Program")
    print()

    while True:
        capacity = float(input("Enter the capacity of the barrel: "))
        barrel = Barrel(capacity)
        
        while True:
            type = input("Enter apple type: ")
            weight = float(input("Enter apple weight: "))
            price = float(input("Enter apple price: "))
            
            apple = Apple(type, weight, price)
            barrel.add_apple(apple)
            
            choice = input("Add more apples? (y/n): ")
            print()
            if choice != "y":
                print('Your barrel has these apples:')
                print(barrel)
                break
        
        choice = input("Get another barrel? (y/n): ")
        print()
        if choice != "y":
            print("Bye!")
            break
        

if __name__ == "__main__":
    main()