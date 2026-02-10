# Aiden Munger
# 1/29/2026
# Book class Demo OOP
# Library System

from typing import Any


class Book:
    def __init__(self, title : str, checked_out : bool = False):
        self.title = title
        self.checked_out = checked_out
        
    def check_out(self):
        self.checked_out = True
    
    def return_book(self):
        self.checked_out = False

    def __eq__(self, other: Any) -> bool:
        # We get to define how two Books are compared for equality.
        return self.title == other.title

    def __str__(self):
        str_rep = f"{self.title}, checked out: {self.checked_out}"
        
        return str_rep
    
hp1 = Book("Harry Potter and the Sorcerer's Stone")
#print(hp1)
#hp1.check_out()
#print(hp1)

hp1.return_book()
#print(hp1)


book_shelf: list[Book] = [hp1, Book("Harry Potter and the Chamber of Secrets"), Book("Harry Potter and the Prisoner of Azkaban"), Book("Harry Potter and the Goblet of Fire"), Book("Harry Potter and the Order of the Phoenix"), Book("Harry Potter and the Half-Blood Prince"), Book("Harry Potter and the Deathly Hollow")]

for i in range(len(book_shelf)):
    print(i)
    book_shelf[i].check_out()
    print(book_shelf[i])
    print()

print(hp1 == book_shelf[0])
print(hp1 is book_shelf[0])
#hp1_copy = copy.copy(hp1)
#print(hp1 == hp1_copy)
#print(hp1 is hp1_copy)