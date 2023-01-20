class Customer:
    def __init__(self, account_no: int, first_name: str, last_name: str, balance: float) -> None:
        self.__account_no: int = account_no
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__balance: float = balance

    def __str__(self) -> str:
        return f"Customer account no = {self.__account_no}, first name = {self.__first_name}, last name = {self.__last_name}, balance = {self.__balance}"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Customer):
            return self.__account_no == __o.__account_no
        return False

    @property
    def account_no(self) -> int:
        return self.__account_no
    @property
    def first_name(self) -> str:
        return self.__first_name
    @property
    def last_name(self) -> str:
        return self.__last_name
    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance