from typing import List

from bank import Bank
from customer import Customer


class BankApp:
    def __init__(self) -> None:
        self.__bank: Bank = Bank("SFBU Bank")

    def show_program_title(self) -> None:
        print("The Bank Application for", self.__bank.bankname)

    def show_menu(self) -> int:
        print("\nCommand Menu")
        print("1.   Print customer forward")
        print("2.   Print customer backward")
        print("3.   Search customer by account no")
        print("4.   Update customer details")
        print("5.   Remove customer record")
        print("6.   Print customer info by last name")
        print("7.   Find biggest account balace")
        print("8.   Find smallest account balace")
        print("9.  Add new customer")
        print("10.  Exit")
        command_no: int = int(input("Enter your choice: "))
        print()
        return command_no

    def execute_command(self, commnad_no: int) -> bool:
        done: bool = False
        if commnad_no == 1:
            self.__bank.print_forward()

        if commnad_no == 2:
            self.__bank.print_backward()

        if commnad_no == 3:
            customer: Customer | None = self.__bank.get_customer_by_accountno(int(input("Enter account number of the customer: ")))
            if customer is None:
                return done        
            print(customer)
        
        if commnad_no == 4:
            customer: Customer | None = self.__bank.get_customer_by_accountno(int(input("Enter account number: ")))
            if customer is None:
                return done
            opt: int = 0
            if customer:
                opt = int(input(f"Customer details: \n1. First Name: {customer.first_name}, \n2. Last Name: {customer.last_name} and \n3. Balance: {customer.balance}, \nPlease select the option which you would like to update"))
            
            if opt == 1:
                first_name: str = input("Please enter the new first name: ")
                self.__bank.update_customer(customer.account_no, first_name, customer.last_name, customer.balance)
            elif opt == 2:
                last_name: str = input("Please enter the new last name: ")
                self.__bank.update_customer(customer.account_no, customer.first_name, last_name, customer.balance)
            elif opt == 3:
                balance: float = float(input("Please enter the new balance: "))
                self.__bank.update_customer(customer.account_no, customer.first_name, customer.last_name, balance)


        if commnad_no == 5:
            customer: Customer | None = self.__bank.get_customer_by_accountno(int(input("Enter account number")))
            if customer is None:
                return done
            self.__bank.remove_customer(customer.account_no)

        if commnad_no == 6:
            last_name = input("Enter the last name to be searched")
            customers: List[Customer] = self.__bank.get_customers_by_lastname(last_name)
            print("Customer details:")
            for cust in customers:
                print(cust)

        if commnad_no == 7:
            cust: Customer | None = self.__bank.get_customer_with_highest_pay()
            if cust:
                print(cust)

        if commnad_no == 8:
            cust: Customer | None = self.__bank.get_customer_with_lowest_pay()
            if cust:
                print(cust)

        if commnad_no == 9:
            acc_no: int = int(input("Please enter account number"))
            f_name: str = input("Please enter first name")
            l_name: str = input("Please enter last name")
            balance: float = float(input("Please enter initial balance"))
            self.__bank.add_customer(acc_no, f_name, l_name, balance)

        if commnad_no == 10:
            done = True

        return done
        

def main() -> None:
    app: BankApp = BankApp()
    app.show_program_title()
    stop_exec = False
    while not stop_exec:
        command_no: int = app.show_menu()
        stop_exec: bool =app.execute_command(command_no)

if __name__=="__main__":
    main()
