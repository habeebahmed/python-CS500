# Write a Python program to define the following small methods:

# Write a method called smaller_than(limit,numbers) that takes as inputs a number limit and a list of numbers values, and that returns the list of elements of numbers that are smaller than limit. You must use a list comprehension for this method.

# Write a method called long_words(num, wordList) that takes as inputs an integer num and a list of strings word_list, and that uses a list comprehension to construct and return a list consisting of all words from wordList that are longer than num. For example:
#     long_words(4, ['apple', 'bus', 'lamp', 'tie', 'orange'])

# [‘apple’', 'orange’’]

# Based on the following examples, use the reduce function and the list comprehension to write this method named get_code(word_list)
#     word_list = ['hello', 'world', 'how', 'goes', 'tears']

#     => 55345

#     word_list = [‘apple’, 'orange', 'banana ', 'pears ', 'lemon']

#     => 56655

from typing import List
from functools import reduce


def smaller_than(limit: float,numbers: List[float]):
    return [ x for x in numbers if x < limit]

def long_words(num: int, wordList: List[str]):
    return [ x for x in wordList if len(x) > num ]

def get_code(word_list: List[str]):
    code_list: list[int] = [ str(len(x.strip())) for x in word_list ]

    return reduce(lambda prev, next: prev + next, code_list)


def main():
    print("Smaller than limit test")
    smaller_list = smaller_than(5, [1,2,3,8,9,10])
    print(smaller_list)


    print("\n\nLong words test")
    long_word_list = long_words(4, ['apple', 'bus', 'lamp', 'tie', 'orange'])
    print(long_word_list)

    print("\n\nget_code test")
    code = int(get_code(['hello', 'world', 'how', 'goes', 'tears']))
    print(code)
    code = int(get_code(['apple', 'orange', 'banana ', 'pears ', 'lemon']))
    print(code)


if __name__ == "__main__":
    main()