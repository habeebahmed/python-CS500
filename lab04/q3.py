# Implement a class named Month whose objects represent months.
# ● Data member:
#     ○ month_number: represents a unique month of the year. i.e. 0 <= month_number < 12
# ● Constructor takes a string argument (e.g. January, February, .... , or
# December) so it needs to converts it to month_number.
# ● Other public methods:
#     ○ advance(self); advances to the next month
#     ○ prev(self); go back to the previous month.
#     ○ display(self) that prints the month_number in string i.e. January, February, .... , or December
#     ○ compare(m: Month) that takes a Month object,
#         ■ if this object is greater than the m object, returns 1.
#         ■ if this object is greater than the m object, returns -1
#         ■ if this object is equal to the m object, returns 0.
# ● Write a main() function to test your Month class.
from __future__ import annotations
from typing import Literal

class Month:
    def __init__(self, month: str) -> None:
        self.month_dict: dict[int, str] = {0: 'January', 1: 'February', 2: 'March', 3: 'April', 4: 'May', 5: 'June', 6: 'July', 7: 'August', 8: 'September', 9: 'October', 10: 'November', 11: 'December'}
        self.month_number = list(self.month_dict.keys())[list(self.month_dict.values()).index(month)]
    
    def advance(self) -> None:
        self.month_number = self.month_number + 1 if self.month_number + 1 <= 11 else 0
    
    def prev(self) -> None:
        self.month_number: int = self.month_number - 1 if self.month_number - 1 >= 0 else 11

    def display(self) -> None:
        print(self.month_dict[self.month_number])

    def compare(self, m: Month) -> Literal[1, -1, 0]:
        if self.month_number > m.month_number :
            return 1
        elif self.month_number < m.month_number :
            return -1
        else:
            return 0


def main() -> None:
    month1: Month = Month('November')

    month1.display()
    
    # advance the month
    month1.advance()
    month1.advance()
    month1.advance()
    month1.display()

    # prev the month
    month1.prev()
    month1.display()

    # Other month for comparision
    month2: Month = Month('February')

    month2.prev()

    print("Compare result: ", month1.compare(month2))

if __name__ == "__main__":
    main()