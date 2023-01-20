import csv
from typing import List

from customer import Customer


# Handle the customers csv file
class CustomerRepository:
    def __init__(self, filename: str = "customers.csv") -> None:
        self.__filename: str = filename

    # read customers from the data file
    def get_customer(self) -> List[Customer]:
        customers: list[Customer] = []
        with open(self.__filename, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                customer: Customer = Customer(
                    int(row[0]), # account_no
                    row[1], # first_name
                    row[2], # last_name
                    float(row[3])   # balance
                )
                customers.append(customer)
            return customers

    # write customers to the data file
    def save_customers(self, customers: List[Customer]) -> None:
        with open(self.__filename, "w", newline="") as file:
            writer = csv.writer(file)
            rows: list[list[str | int | float]] = []
            for customer in customers:
                rows.append([customer.account_no, customer.first_name, customer.last_name, customer.balance])
            
            writer.writerows(rows)


def main() -> None:
    db: CustomerRepository = CustomerRepository()
    customers: List[Customer] = db.get_customer()
    print(customers)

    customers[0].balance = 50000

    db.save_customers(customers)

if __name__=="__main__":
    main()