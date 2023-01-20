from typing import List, Optional

from customer import Customer
from db import CustomerRepository


class Bank:
    def __init__(self, bankname: str) -> None:
        self.__bankname: str = bankname
        self.__customers: list[Customer] = []
        self.read_customers_from_db()

    
    @property
    def bankname(self) -> str:
        return self.__bankname

    def add_customer(self, account_no: int, first_name: str, last_name: str, balance: float) -> None:
        cust: Customer = Customer(account_no, first_name, last_name, balance)
        self.__customers.append(cust)
        self.save_customer_to_db()

    def remove_customer(self, account_no: int) -> None:
        index: int = next((index for (index, d) in enumerate(
            self.__customers) if d.account_no == account_no), -1)
        if index != -1:
            self.__customers.pop(index)
            self.save_customer_to_db()

    def get_customer_by_accountno(self, account_no: int) -> Optional[Customer]:
        index: int = next((index for (index, d) in enumerate(
            self.__customers) if d.account_no == account_no), -1)
        if index != -1:
            return self.__customers[index]

    def update_customer(self, account_no: int, first_name: str, last_name: str, balance: float) -> None:
        cust: Customer = Customer(account_no, first_name, last_name, balance)
        index: int = next((index for (index, d) in enumerate(
            self.__customers) if d.account_no == cust.account_no), -1)
        if index != -1:
            self.__customers[index] = cust
            self.save_customer_to_db()

    def get_customers_by_lastname(self, last_name: str) -> List[Customer]:
        customer_list: list[Customer] = list(
            filter(lambda x: x.last_name == last_name, self.__customers))
        return customer_list
    
    def get_customer_with_highest_pay(self) -> Optional[Customer]:
        max_sal_cust: Customer | None = None
        for cust in self.__customers:
            if max_sal_cust is None:
                max_sal_cust = cust
            elif cust.balance > max_sal_cust.balance:
                max_sal_cust = cust
        return max_sal_cust

    def get_customer_with_lowest_pay(self) -> Optional[Customer]:
        min_sal_cust: Customer | None = None
        for cust in self.__customers:
            if min_sal_cust is None:
                min_sal_cust = cust
            elif cust.balance < min_sal_cust.balance:
                min_sal_cust = cust
        return min_sal_cust

    def read_customers_from_db(self) -> None:
        db: CustomerRepository = CustomerRepository()
        self.__customers = db.get_customer()

    def save_customer_to_db(self) -> None:
        db: CustomerRepository = CustomerRepository()
        db.save_customers(self.__customers)

    def print_forward(self) -> None:
        sorted_list_asc: list[Customer] = sorted(self.__customers, key = lambda x: x.account_no)
        print("Sorted customer list in forward direction for bank: ", self.__bankname)
        for cust in sorted_list_asc:
            print(cust)
            # print(f"\nCustomer detail:\naccount no: {cust.account_no}\nFirst Name: {cust.first_name}\nLast Name: {cust.last_name}\nBalance: {cust.balance}")

    def print_backward(self) -> None:
        print("Sorted customer list in backward direction for bank: ", self.__bankname)
        sorted_list_desc: list[Customer] = sorted(self.__customers, key = lambda x: x.account_no, reverse=True)
        for cust in sorted_list_desc:
            print(cust)

