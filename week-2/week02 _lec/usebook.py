#!/usr/bin/env python3

from bookstore import Book

b1 = Book('How to C++', 'Peter', 50)
b2 = Book('Python Programming')

print('b1 =', str(b1))
print('b2 =', str(b2))
print()
b2.setAuthor('Lily')
b2.price = 56.7
print("After b2.setAuthor('Lily') and b2.price = 56.7")
print('b2 =', str(b2))
print()
b2.title = 'Advanced C'
print("After b2.title = 'Advanced C'")
print('b2 =', str(b2))
print()
b2.setTitle('Advanced C')
print("b2.setTitle('Advanced C')'")
print('b2 =', str(b2))
